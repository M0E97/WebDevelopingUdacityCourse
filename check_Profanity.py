import urllib
def read_txt():
    quotes=open("/home/mohamed97/Downloads/movie-quotes/movie_quotes/movie_quotes.txt")
    content=quotes.read()
    check_profanity(content)
    quotes.close()
def check_profanity(txt):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+txt)
    output=connection.read()
    if "True" in output:
        print "Profanity Alert"
    else:
        print "no curse word "
    connection.close()

read_txt()