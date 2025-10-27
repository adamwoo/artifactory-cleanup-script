{
  "files": [
    {
      "aql": {
        "items.find": {
          "name": {"$match":"*"},
          "created": { "$before":"30d" },
          "modified": { "$before":"30d" },
          "repo": {"$nmatch":"*-release"},
          "@cleanup.skip":{"$ne":"true"},
          "$or":[
            {
              "$and": [
                {"stat.downloads": {"$eq": null}},
                {"repo": {"$match":"*repo-local*"}},
                {"path": {"$match":"yourpath/*"}}
              ]
            }
          ]
        }
      }
    }
  ]
}
