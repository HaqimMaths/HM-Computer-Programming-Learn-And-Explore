# R basics exercises Part One
# By Haqim Maths on 2024, December 21th
# Section 1
name <- readline(prompt = "Enter your name here: ")
age <- readline(prompt = "How old are you?: "); age <- as.integer((age))
print(paste("Your name is ", name , " and you are ", age ," years old!"))
# Section 2
print(ls())
print(ls.str())

# Section 3
seq(20, 50)
paste("Mean: ", mean(seq(20, 60)))
paste("Sum from 51 - 91: ", sum(seq(51, 91)))

# Section 4
paste("Random integer between -50 and 50 are: ", sample(-50:50, 10, replace=TRUE))

# Section 5 (First 10 Fibonacci Numbers)

# Section 6 (Prime numbers)

# Section 7 (Print 100 Numbers)

one_until_hundred = seq(1, 100)
for (i in one_until_hundred){
 if(i %% 3 == 0 & i %% 5 != 0){
  print("Fizz")
 } else if (i %% 3 != 0 & i %% 5 == 1){
  print("Buzz")
 } else if (i %% 3 == 0 & i %% 5 == 1){
  print("FizzBuzz")
 } else {
  print(i)
 }
}

# Section 8 (Extract 10 english letter)

# Section 9 (Factorial)
n = readline(prompt = "Enter an integer: ")
n = as.integer(n)
factorialResult <- 1
i <- 0
while(i <= n){
 if (i == 0){
  print("skip 0")
 }
 else{
  factorialResult <- factorialResult * i
 }
 i <- i + 1
}; print(factorialResult)
# Section 10 (Max and Min)
vector_one <- c(10:100)
paste("Max and min in vector_one: ", max(vector_one), " | ", min(vector_one))

