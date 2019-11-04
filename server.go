
package main

import (
  "io"
  "io/ioutil"
  "log"
  "net/http"
  "encoding/json"
)

type Benchmark struct {
  Bench string `json:"bench"` // Uppercased first letter
  Suite string `json:"age"`   // Uppercased first letter
}

func main() {

  h1 := func(w http.ResponseWriter, r *http.Request) {
    body, _ := ioutil.ReadAll()
    // exec("java -jar similar-code-search.jar bruno-index output/stats.txt output/similar.json");
    // json.Unmarshal(body, &p)
    io.WriteString(w, "Hello from a HandleFunc #1!\n")
  }


  http.HandleFunc("/", h1)

  log.Fatal(http.ListenAndServe(":8080", nil))
}
