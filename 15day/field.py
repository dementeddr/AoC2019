#! /bin/usr/env python3

class coord:

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, coord):
            return NotImplemented
        return (self.x == other.x and self.y == other.y)

#END OF CLASS


class Field:

    def display(self, mapping = {}):

        if len(mapping) == 0:
            for row in self.plane:
                print(row)
            return
        
        print('_')

        for row in self.plane:
            outstr = '|'

            for val in row:
                if val in mapping:
                    outstr += mapping[val]
                else:
                    outstr += ' '

            outstr += '|'
            print(outstr)

        print("=")


    def get_full(self):
        ret = self.plane
        return ret

    def expand_up(self, target):
        
        while target.y < 0:
            delta = len(self.plane)
            
            new_area = [[0 for row in range(len(self.plane[0]))] for col in range(len(self.plane))]
            self.plane = new_area + self.plane
            
            target.y += delta
            self.center.y += delta



    def expand_down(self, target):

        while len(self.plane) <= target.y:
            delta = len(self.plane)
            
            new_area = [[0 for row in range(len(self.plane[0]))] for col in range(len(self.plane))]
            self.plane = self.plane + new_area
        


    def expand_left(self, target):
        
        while target.x < 0:
            delta = len(self.plane[0])
        
            for row in range(len(self.plane)):
                new_area = [0 for col in range(delta)]
                self.plane[row] = new_area + self.plane[row]

            target.x += delta
            self.center.x += delta



    def expand_right(self, target):
        
        while len(self.plane[0]) <= target.x:
            delta = len(self.plane[0])

            for row in range(len(self.plane)):
                new_area = [0 for col in range(delta)]
                self.plane[row] = self.plane[row] + new_area


    def get_val(self, arg1, arg2=None):

        target = arg1

        if arg2 is not None:
            target = coord(arg1, arg2)

        abs_coord = coord(self.center.x + target.x, self.center.y - target.y)

        if (abs_coord.x < 0 or abs_coord.y < 0 
            or abs_coord.x >= len(self.plane[0]) or abs_coord.y >= len(self.plane)):

            return 0

        else:
            return self.plane[abs_coord.y][abs_coord.x]

    
    def set_val(self, val, arg1, arg2=None):

        target = arg1

        if arg2 is not None:
            target = coord(arg1, arg2)    

        abs_coord = coord(self.center.x + target.x, self.center.y - target.y)
        #print(f"{target} = {abs_coord}")

        if abs_coord.y >= len(self.plane):
            self.expand_down(abs_coord)

        if abs_coord.y < 0:
            self.expand_up(abs_coord)

        if abs_coord.x >= len(self.plane[0]):
            self.expand_right(abs_coord)

        if abs_coord.x < 0:
            self.expand_left(abs_coord)
    
        self.plane[abs_coord.y][abs_coord.x] = val

    

    def __init__(self, init_radius = 2):
        
        self.plane = [[0 for row in range(init_radius*2 + 1)] for col in range(init_radius*2 + 1)]
        self.center = coord(init_radius, init_radius)

#END OF CLASS


def main():

    f = Field()
    f.plane[2][2] = 1
    #f.set_val(-4, -4, 2)
    f.set_val(2, 4, 10)
    print(f.get_val(4, 10))
    f.display()

if __name__ == "__main__":
    main()
