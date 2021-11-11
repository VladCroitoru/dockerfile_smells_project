package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main()  {
	fileName := os.Args[1]
	dataset := os.Args[2]
	repos, err := os.Open(fileName)
	if err != nil {
		log.Fatalln(err)
	}
	defer repos.Close()

	i := 0
	scanner := bufio.NewScanner(repos)
	for scanner.Scan() {
		i += 1
		repo := scanner.Text()
		url := fmt.Sprintf("https://raw.githubusercontent.com/%s/master/Dockerfile", repo)
		resp, err := http.Get(url)
		if err != nil {
			log.Fatalln(err)
		}
			
		log.Printf("progress: %d/60831, code: %d, repo: %s \n", i, resp.StatusCode, repo)
		if resp.StatusCode == 200 {
			dir := fmt.Sprintf("%s/%s", dataset, repo)
			err = os.MkdirAll(dir, os.ModePerm)
			if err != nil {
				log.Fatalln(err)
			}
			f, err := os.Create(fmt.Sprintf("%s/%s/Dockerfile", dataset, repo))
			if err != nil {
				log.Fatalln(err)
			}
			
			body, _ := ioutil.ReadAll(resp.Body)
			_, err = f.Write(body)
			if err != nil {
				log.Fatalln(err)
			}
			f.Close()
		}
	}
}
