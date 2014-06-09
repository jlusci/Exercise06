#from sys import argv

def main():
    restaurant_reviews = {}
    f = open('scores.txt')
    for line in f:
        line = line.rstrip()
       
        restaurant, score = line.split(':')

        restaurant_reviews[restaurant] = score

    f.close()    

    print restaurant_reviews



if __name__ == "__main__":
    main()