/*
  Section: OOP
  Topic: File class
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
*/

class File {
  constructor(name, size, type) {
    this.name = name;
    this.size = size;
    this.type = type;
  }

  info() {
    console.log(`Name: ${this.name}, Size: ${this.size}KB, Type: ${this.type}`);
  }
}

let file1 = new File('Document', 100, 'PDF');
file1.info();