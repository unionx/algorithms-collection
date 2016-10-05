package main

import (
	"fmt"
	"regexp"
	"log"
	"bufio"
	"os"
	"strings"
)

func replaceString(str, replace, to string) string {
	reg, err := regexp.Compile(replace)
	if err != nil {
		log.Fatal(err)
	}

	return reg.ReplaceAllString(str, to)
}

func readInput(filename string) (string, []string) {
	dna := ""
	thisIntron := ""
	introns := []string{}
	headerCount := 0

	f, _ := os.Open(filename)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, ">") {
			if headerCount != 1 {
				introns = append(introns, thisIntron)
				thisIntron = ""
			}

			headerCount += 1
			continue
		}

		if strings.Compare(dna, "") == 0 {
			dna = line
		} else {
			if headerCount == 1 {
				dna = dna + line
			} else {
				thisIntron = thisIntron + line
			}
		}
	}

	introns = append(introns, thisIntron)
	return dna, introns
}

func main() {
	dna, introns := readInput("./datasets/rosalind_splc.txt")
	// fmt.Println(dna)
	// fmt.Println(introns)
	for _, intron := range introns {
		dna = replaceString(dna, intron, "")
	}

	dna = replaceString(dna, "T", "U")
	fmt.Println(dna)
}
