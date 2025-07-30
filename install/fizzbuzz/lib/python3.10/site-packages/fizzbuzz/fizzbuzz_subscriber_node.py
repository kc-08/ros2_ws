import rclpy
from rclpy.node import Node

# import our new fizzbuzz message type
from fizzbuzz_interfaces.msg import FizzBuzz 
from std_msgs.msg import Int32

# TODO import the number message used for the numbers topic

class FizzBuzzNode(Node):
    def __init__(self):
        super().__init__('fizzbuzz')
        self.get_logger().info("Starting fizzbuzz node")

        self.total_numbers = 0
        self.total_fizz = 0
        self.total_buzz = 0
        self.total_fizzbuzz = 0

        # create a publisher object to send data
        self.fizzbuzz_pub = self.create_publisher(FizzBuzz, "fizzbuzz_stats", 10)

        # TODO fill in the TOPIC_NAME and MESSAGE_TYPE
        self.number_sub = self.create_subscription(Int32, "numbers", self.number_callback, 10)

    def number_callback(self, msg):
        # this function is called whenever a number is received.

        number = msg.data 

        fizzbuzz_str = self.fizzbuzz(number)
        
        self.total_numbers += 1

        if fizzbuzz_str == 'fizz':
            self.total_fizz += 1
        elif fizzbuzz_str == 'buzz':
            self.total_buzz += 1
        elif fizzbuzz_str == 'fizzbuzz':
            self.total_fizzbuzz += 1

        # loginfo to print the string to the terminal
        self.get_logger().info(fizzbuzz_str)

        fizzbuzz_msg = FizzBuzz()
        fizzbuzz_msg.fizzbuzz = fizzbuzz_str
        fizzbuzz_msg.fizz_ratio = 0.0 if self.total_fizz == 0 or self.total_numbers - self.total_fizz == 0 else self.total_fizz/ (self.total_numbers - self.total_fizz) # TODO fill in this value
        fizzbuzz_msg.buzz_ratio = 0.0 if self.total_buzz == 0 or self.total_numbers - self.total_buzz == 0 else self.total_buzz/ (self.total_numbers - self.total_buzz) # TODO fill in this value
        fizzbuzz_msg.fizzbuzz_ratio = 0.0 if self.total_fizzbuzz == 0 or self.total_numbers - self.total_fizzbuzz == 0 else self.total_fizzbuzz/ (self.total_numbers - self.total_fizzbuzz) # TODO fill in this value
        fizzbuzz_msg.number_total = self.total_numbers # TODO fill in this value

        # publish the message
        self.fizzbuzz_pub.publish(fizzbuzz_msg)

    def fizzbuzz(self, number):
        if number % 3 == 0:
            if number % 5 == 0:
                return 'fizzbuzz'
            else:
                return 'fizz'
        elif number % 5 == 0:
            return 'buzz'
        else:
            return ''
        # TODO complete this function
        # This should return a string equal to:
        #      "fizz" if number divisible my 3
        #      "buzz" if number divisible my 5
        #      "fizzbuzz" if number divisible my 15
        #      an empty string otherwise
        #return ""


def main(args=None):
    rclpy.init()
    node = FizzBuzzNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()