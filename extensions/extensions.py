def main():
    extend = input("Provide a input? ").strip().lower()
    extension(extend)

def extension(extend):
        if extend.endswith(".gif"):
            print("image/gif")
        elif extend.endswith(".jpg") | extend.endswith(".jpeg"):
            print("image/jpeg")
        elif extend.endswith(".png"):
            print("image/png")
        elif extend.endswith(".pdf"):
            print("application/pdf")
        elif extend.endswith(".txt"):
            print("text/plain")
        elif extend.endswith(".zip"):
            print("application/zip")
        else:
            print("application/octet-stream")
main()

