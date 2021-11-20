package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"
)

func buildRequest(url, token string) *http.Request {
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("Authorization", fmt.Sprintf("token %s", token))
	return req
}

// get token rate limit from github api
func getRateLimit(token string) int {
	client := &http.Client{}
	fmt.Println(fmt.Sprintf("checking rate limit for token: %s", token))
	resp, err := client.Do(buildRequest("https://api.github.com/rate_limit", token))
	if err != nil {
		fmt.Println(err)
		return 0
	}
	defer resp.Body.Close()
	remaining, _ := strconv.Atoi(resp.Header.Get("X-RateLimit-Remaining"))
	fmt.Println(fmt.Sprintf("remaining api calls for token: %s is - %d", token, remaining))
	return remaining
}

func readLines(path string, n int) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
		if len(lines) >= n {
			break
		}
	}
	return lines, scanner.Err()
}

// write string to file, if file missing create
func writeFile(pathRoot, repo string, text string) {
	path := fmt.Sprintf("./%s/%s", pathRoot, repo)
	err := os.MkdirAll(path, os.ModePerm)
	if err != nil {
		log.Fatalln(err)
	}

	file, err := os.OpenFile(path+"/Dockerfile.contributors.json", os.O_CREATE|os.O_WRONLY, 0755)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()
	
	if _, err := file.WriteString(text); err != nil {
		fmt.Println(err)
		return
	}
}

// create file then append string to file
func writeVisited(visitedPath, repo string) {
	file, err := os.OpenFile(visitedPath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0755)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()
	
	if _, err := file.WriteString(repo+"\n"); err != nil {
		log.Fatalln(err)
	}
}

func fetchContributors(repos []string, token, outputPath, visitedPath string) {
	client := &http.Client{}
	for _, repo := range repos {
		log.Println(fmt.Sprintf("getting contributors for %s", repo))
		url := fmt.Sprintf("https://api.github.com/repos/%s/contributors", repo)
		resp, err := client.Do(buildRequest(url, token))
		if err != nil {
			fmt.Println(err)
			continue
		}
		defer resp.Body.Close()

		if resp.StatusCode == 200 {
			body, _ := ioutil.ReadAll(resp.Body)
			writeFile(outputPath, repo, string(body))
			writeVisited(visitedPath, repo)
		} else {
			log.Println(fmt.Sprintf("ERROR, could not retrieve %s data - %s", repo, resp.Status))
		}
	}
}

func readVisited(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func readRepos(path string) []string {
	repos, err := os.Open(path)
	if err != nil {
		log.Fatalln(err)
	}
	defer repos.Close()

	var lines []string
	scanner := bufio.NewScanner(repos)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			lines = append(lines, strings.Split(line, " ")[0])
		}
	}
	return lines
}

func readTokens(path string) []string {
	tokens, err := os.Open(path)
	if err != nil {
		log.Fatalln(err)
	}
	defer tokens.Close()

	var lines []string
	scanner := bufio.NewScanner(tokens)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" && !strings.HasPrefix(line, "//") {
			lines = append(lines, strings.Split(line, " ")[0])
		}
	}
	return lines
}

// filter duplicates from a list based on a second list
func filter(list []string, filter []string) []string {
	var filtered []string
	for _, item := range list {
		if !contains(filter, item) {
			filtered = append(filtered, item)
		}
	}
	return filtered
}

// check if a list contains a string
func contains(list []string, item string) bool {
	for _, val := range list {
		if val == item {
			return true
		}
	}
	return false
}

// return first n item from a list skip offset
func slice(list []string, n int, offset int) []string {
	var sliced []string
	for i, item := range list {
		if i >= offset && i < offset+n {
			sliced = append(sliced, item)
		}
	}
	return sliced
}

func main() {
	fmt.Println("starting")
	reposFile := os.Args[1]
	visitedPath := os.Args[2]
	outputPath := os.Args[3]
	tokens := readTokens(".gh_tokens")
	repos := readRepos(reposFile)
	visited := readVisited(visitedPath)
  toVisit := filter(repos, visited)
	fmt.Println(fmt.Sprintf("repos %d", len(repos)))
	fmt.Println(fmt.Sprintf("visited %d", len(visited)))
	fmt.Println(fmt.Sprintf("toVisit %d", len(toVisit)))

	offset := 0
	var wg sync.WaitGroup
	for _, token := range tokens {
		remaining := getRateLimit(token)
		if remaining > 0 {
			repos := slice(toVisit, remaining, offset)
			offset += len(repos)
			fmt.Println(fmt.Sprintf("offset: %d", offset))
			
			wg.Add(1)
			go func ()  {
				fetchContributors(repos, token, outputPath, visitedPath)
				defer wg.Done()
			}()
		}
	}
	wg.Wait()
}
