"""Restaurant rating lister."""
def make_ratings_dict(file_name):
    """ Display the rating for each restaurant in file """
    ratings_text = open(file_name)
    ratings_dict = {}
    for line in ratings_text:
        # print(line)
        item = line.rstrip().split(":")
        key = item[0]
        value = item[1]
        ratings_dict[key] = value
    # Ask user for input
    restaurant_entry = input("Please enter a restaurant: ")
    rating_entry = input("Please enter a rating: ")
    ratings_dict[restaurant_entry] = rating_entry
    ratings_list = ratings_dict.items()
    sorted_ratings = sorted(ratings_list)
    for restaurant in range(len(sorted_ratings)):
        print(f'{sorted_ratings[restaurant][0]} is rated at {sorted_ratings[restaurant][1]}.')

make_ratings_dict("scores.txt")
