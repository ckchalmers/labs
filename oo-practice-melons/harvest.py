############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller
        ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType( 
        "musk",
        "Muskmelon",
         1998,
        "green",    
        True,
        True
        )
    musk.add_pairing("mint")
    all_melon_types.append(musk)


    cas = MelonType(
        "cas",
        "Casaba",
        2003,
        "orange",
        False,
        False
    )
    cas.add_pairing("strawberries")
    cas.add_pairing("mint") 
    all_melon_types.append(cas)
    

    cren = MelonType(
        "cren",
        "Crenshaw",
        1996,
        "green",
        False,
        False
    )
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)


    yw = MelonType(
        "yw",
        "Yellow Watermelon",
        2013,
        "yellow",
        False,
        True
    )
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    # for melon in all_melon_types:
        # print(melon)
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    return {melon.code:melon for melon in melon_types}


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self, melon_type, shape_rating, color_rating, from_field, harvested_by
        ):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by= harvested_by
        
    def is_sellable(self):
        """Returns True or False based on whether the melon is able to be sold"""
        self.sellable = self.shape_rating > 5 and self.color_rating > 5 and self.from_field != 3
            
def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melons = []

    melons_by_id = make_melon_type_lookup(melon_types)
    
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, "Sheila")
    melon_1.is_sellable()
    all_melons.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, "Sheila")
    melon_2.is_sellable()
    all_melons.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, "Sheila")
    melon_3.is_sellable()
    all_melons.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, "Sheila")
    melon_4.is_sellable()
    all_melons.append(melon_4)
    
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, "Michael")
    melon_5.is_sellable()
    all_melons.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, "Michael")
    melon_6.is_sellable()
    all_melons.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, "Michael")
    melon_7.is_sellable()
    all_melons.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, "Michael")
    melon_8.is_sellable()
    all_melons.append(melon_8)
    
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, "Sheila")
    melon_9.is_sellable()
    all_melons.append(melon_9)

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.sellable:
            print(f"Havested by {melon.harvested_by} from Field {melon.from_field} (CAN BE SOLD)")
        else:
            print(f"Havested by {melon.harvested_by} from Field {melon.from_field} (NOT SELLABLE)")
        
def make_melons_from_file(file_name):
    """Returns a list of Melon objects."""

    all_melons_in_file = []

    melons_by_id = make_melon_type_lookup(make_melon_types())

    file_contents = open(file_name)
    for line in file_contents:
        record = line.split(' ')
        shape_rating = int(record[1])
        color_rating = int(record[3])
        melon_type = melons_by_id[record[5]]
        harvested_by = record[8]
        from_field = int(record[11])
        all_melons_in_file.append(Melon(melon_type, shape_rating, color_rating, from_field, harvested_by))

    for melon in all_melons_in_file:
        melon.is_sellable()
    
    return all_melons_in_file

#def main():
# make_melon_types()
#print_pairing_info(make_melon_types())
#print(make_melon_type_lookup(make_melon_types()))
#print(make_melons(make_melon_types()))
get_sellability_report(make_melons_from_file("harvest_log.txt"))
#get_sellability_report(make_melons(make_melon_types()))
# if __name__ == "__main__":
    # main()