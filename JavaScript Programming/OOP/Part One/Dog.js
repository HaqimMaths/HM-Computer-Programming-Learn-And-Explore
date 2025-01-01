/*
  Section: OOP
  Topic: Dog class
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
*/

class Dog {
  constructor(name, breed, age) {
    this.name = name;
    this.breed = breed;
    this.age = age;
  }

  bark() {
    console.log('Woof! Woof!');
  }

  info() {
    console.log(`Name: ${this.name}, Breed: ${this.breed}, Age: ${this.age}`);
  }
}

let dog1 = new Dog('Buddy', 'Golden Retriever', 5);
dog1.bark();
dog1.info();
let dog2 = new Dog('Daisy', 'Beagle', 3);
dog2.bark();
dog2.info();