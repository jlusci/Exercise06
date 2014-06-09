#from sys import argv

def main():
    restaurant_reviews = {}
    f = open('scores.txt')
    for line in f:
        line = line.rstrip()
       
        restaurant, score = line.split(':')

        restaurant_reviews[restaurant] = score

    f.close()    

    #print restaurant_reviews
    #print sorted(restaurant_reviews)
    # print restaurant_reviews.iteritems()

    for key, value in sorted(restaurant_reviews.iteritems()):
        print "Restaurant '%s' is rated at %s." % (key, value) 


if __name__ == "__main__":
    main()