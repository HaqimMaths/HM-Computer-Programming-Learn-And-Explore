/*
  Section: OOP
  Topic: Laptop class
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
*/

class Laptop{
  // Constructor
  constructor(brand, model, price){
    this.brand = brand;
    this.model = model;
    this.price = price;
  }
  // Get details
  display(){
    console.log(`Brand: ${this.brand}, Model: ${this.model}, Price: RM${this.price}`);
  }
}
// Objects
let laptop1 = new Laptop('Apple', 'Macbook Pro', 5000);
let laptop2 = new Laptop('Dell', 'Inspiron', 3000);
let laptop3 = new Laptop('Asus', 'Zenbook', 4000);
let laptop4 = new Laptop('HP', 'Pavilion', 3500);
// Outputs
laptop1.display();
laptop2.display();
laptop3.display();
laptop4.display();