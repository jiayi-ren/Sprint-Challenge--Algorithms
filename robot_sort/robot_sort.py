class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # bubble sort(modified)
        # move right until the end of list
        # compare item, hold the largest until the end of list n
        # move left until the start of list
        # compare item, hold the smallest until 0
        # repeat the process

        # determine total length of list
        length = 1
        # pick up item at index 0
        self.swap_item()
        # move right until the end of list
        # calculate the total length of list
        # move the largest to the end of list
        while self.can_move_right():
            # if item is less than position item, swap
            if self.compare_item() == -1:
                self.swap_item()
            # length + 1
            length += 1
            # move right
            self.move_right()
        # at last item of list
        # if item is larger than last position item, swap
        if self.compare_item() == 1 or self.compare_item() == 0:
            self.swap_item()
        # length == total length of list
        # assign a end index
        end = length - 1
        # assign a start index
        # start index is at None item position
        start = 0
        # robot move between start and end
        # robot at end index now
        # robot move left to start index
        while start < end:
            # move to the start index
            # if encounter None, break loop
            while self.can_move_left():
                self.move_left()
                if self.compare_item() == 1:
                    self.swap_item()
                if self.compare_item() == None:
                    self.swap_item()
                    break
            # start index + 1
            start += 1
            # if start and end next to each other,
            # break out of the loop
            if (end-start) == 1:
                break
            # robot move right
            # position at start index
            self.move_right()
            # swap None with position item
            # None at start index
            self.swap_item()
            # move robot to end index
            # compare and hold largest until the end
            for i in range(end-start-1):
                self.move_right()
                if self.compare_item() == -1:
                    self.swap_item()
            # at end index - 1 position
            # if item is larger than last position item, swap
            if self.compare_item() == 1 or self.compare_item() == 0:
                self.swap_item()
            # end index - 1
            end -= 1
        # if length of index is even
        # last position is at right of mid point of list
        # need to swap item with None
        if length%2 == 0:
            self.swap_item()
        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)