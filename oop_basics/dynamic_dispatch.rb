"""
Code illustrating dynamic dispatching.
"""

class MyClass
  def initialize(name)
    @name = name
  end

  # Dynamically define a greeting method using define_method
  define_method :greeting do
    "Hello, I'm #{@name}!"
  end
end

# Create instances of MyClass
obj1 = MyClass.new("Alice")
obj2 = MyClass.new("Bob")

# Call the dynamically defined greeting method
puts obj1.greeting  # Output: "Hello, I'm Alice!"
puts obj2.greeting  # Output: "Hello, I'm Bob!"
