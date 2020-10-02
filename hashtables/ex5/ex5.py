# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    filepaths = {}
    resultsCache = []

    for filepath in files:
        #split up filepath at slashes "/"
        split_up = filepath.split("/")
        filename = split_up[-1]
        
        if filename in filepaths:
            filepaths[filename].append(filepath)
        else:
            filepaths[filename] = [filepath]
        
    for x in queries:
        if x in filepaths:
            resultsCache.extend(filepaths[x])

    return resultsCache


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
