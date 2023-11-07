const table = document.getElementById("table");
const tableSizeInput = document.getElementById("size");
const generateTableButton = document.getElementById("generateTable");
//const rowInput = document.getElementById("row");
const addRowButton = document.getElementById("addRow");
//const columnInput = document.getElementById("column");
const addColumnButton = document.getElementById("addColumn");
const transposeTableButton = document.getElementById("transposeTable");

generateTableButton.addEventListener("click", generateTable);
addRowButton.addEventListener("click", addRow);
addColumnButton.addEventListener("click", addColumn);
transposeTableButton.addEventListener("click", transposeTable);

function generateTable() {
  const size = parseInt(tableSizeInput.value);

  if (isNaN(size)) {
    alert("Введите правильное значение размера таблицы.");
    return;
  }

  let tableHTML = "";
  for (let i = 0; i < size; i++) {
    tableHTML += "<tr>";
    for (let j = 0; j < size; j++) {
      const randomNumber = Math.floor(Math.random() * 100);
      tableHTML += "<td data-row=" + i + " data-col=" + j + ">" + randomNumber + "</td>";
    }
    tableHTML += "</tr>";
  }
  table.innerHTML = tableHTML;

  addCellClickHandlers();
}

function addRow() {
    //for(let x=0;x<rowInput.value;++x){
      const rowCount = table.rows.length;
      const newRow = table.insertRow(rowCount);
      //const newRow = table.insertRow(-1);

      for (let i = 0; i < table.rows[0].cells.length; ++i) {
        let newCell = newRow.insertCell(i);
        newCell.setAttribute("data-row", rowCount);
        newCell.setAttribute("data-col", i);
        let randomNumber = Math.floor(Math.random() * 100);
        let newText = document.createTextNode(randomNumber);
        newCell.appendChild(newText);
      }

      addCellClickHandlers();
    //}

}
function addColumn() {
  const colCount = table.rows[0].cells.length;

  for (let i = 0; i < table.rows.length; i++) {
    const newCell = table.rows[i].insertCell(colCount);
    newCell.setAttribute("data-row", i);
    newCell.setAttribute("data-col", colCount);
    let randomNumber = Math.floor(Math.random() * 100);
    let newText = document.createTextNode(randomNumber);
    newCell.appendChild(newText);
  }

  addCellClickHandlers();
}

function transposeTable() {
  const rows = Array.from(table.rows);
  const transposedTable = Array.from({ length: rows[0].cells.length }, () =>
    Array.from({ length: rows.length })
  );

  rows.forEach((row, rowIndex) => {
    Array.from(row.cells).forEach((cell, colIndex) => {
      const dataRow = parseInt(cell.getAttribute("data-row"));
      const dataCol = parseInt(cell.getAttribute("data-col"));
      transposedTable[dataCol][dataRow] = cell.textContent;
    });
  });

  let tableHTML = "";
  transposedTable.forEach((row, rowIndex) => {
    tableHTML += "<tr>";
    row.forEach((cellValue, colIndex) => {
      tableHTML += '<td data-row=' + rowIndex + ' data-col=' + colIndex + '>' + cellValue + '</td>';
    });
    tableHTML += "</tr>";
  });
  table.innerHTML = tableHTML;

  addCellClickHandlers();
}

function addCellClickHandlers() {
  const cells = document.querySelectorAll(".JS_table td");
  cells.forEach((cell) => {
    cell.addEventListener("click", () => {
        if(cell.classList.contains('selected')){
            cell.classList.remove("selected");
            cell.classList.remove("selected-even");
            cell.classList.remove("selected-odd");
            return;
        }
console.dir(cell);

      const n = parseInt(document.getElementById("max-select").value);

      let selectedRowCells = table.rows[cell.parentNode.rowIndex].querySelectorAll(".selected");
      if (n > 0 && selectedRowCells.length >= n) {
        console.log("Max in row  " + selectedRowCells.length);

        return;
      }
      //console.log("selectedCells " + cell.cellIndex);

      let selectedColCells = [];
      const colCount = table.rows[0].cells.length;
      for (let i = 0; i < table.rows.length; i++) {
        //console.log(table.rows[i].cells[cell.cellIndex].classList.contains('selected'));

        if(table.rows[i].cells[cell.cellIndex].classList.contains('selected')){
            selectedColCells.push(table.rows[i].cells[cell.cellIndex]);
            //console.log("selectedColCells " + selectedColCells);
        }
      }
      if (n > 0 && selectedColCells.length >= n) {
        console.log("Max in col  " + selectedColCells.length);

        return;
      }

      cell.classList.toggle("selected");
      cell.classList.toggle(
        cell.textContent % 2 === 0 ? "selected-even" : "selected-odd"
      );

      // Check and unselect neighbors
      const dataRow = parseInt(cell.getAttribute("data-row"));
      const dataCol = parseInt(cell.getAttribute("data-col"));

      if (dataRow > 0) {
        unselectNeighbor(dataRow - 1, dataCol);
      }
      if (dataRow < table.rows.length - 1) {
        unselectNeighbor(dataRow + 1, dataCol);
      }
      if (dataCol > 0) {
        unselectNeighbor(dataRow, dataCol - 1);
      }
      if (dataCol < table.rows[0].cells.length - 1) {
        unselectNeighbor(dataRow, dataCol + 1);
      }
    });
  });
}

function unselectNeighbor(row, col) {
  const neighbor = document.querySelector(`td[data-row="${row}"][data-col="${col}"]`);
  if (neighbor) {
    neighbor.classList.remove("selected");
    neighbor.classList.remove("selected-even");
    neighbor.classList.remove("selected-odd");
  }
}
// Ассоциативный массив с данными о книгах
const books = [
    { author: "Автор1", title: "Книга1", year: 1965 },
    { author: "Автор2", title: "Книга2", year: 1970 },
    { author: "Автор1", title: "Книга3", year: 1955 },
    { author: "Автор3", title: "Книга4", year: 1963 },
    { author: "Автор2", title: "Книга5", year: 1944 },
    { author: "Автор3", title: "Книга6", year: 1980 },
];

const bookSearchForm = document.getElementById("bookSearchForm");
const resultDiv = document.getElementById("result");

bookSearchForm.addEventListener("submit", (e) => {
    e.preventDefault();

    // Получаем данные из формы
    const author = document.getElementById("author").value;
    const year = parseInt(document.getElementById("year").value);

    // Фильтруем книги
    const filteredBooks = books.filter(book => {
        return book.author === author && book.year >= year;
    });

    // Выводим результат
    if (filteredBooks.length === 0) {
        resultDiv.innerHTML = "Книг не найдено.";
    } else {
        resultDiv.innerHTML = "Найденные книги:<br>";
        filteredBooks.forEach(book => {
            resultDiv.innerHTML += `Название: ${book.title}, Год издания: ${book.year}<br>`;
        });
    }
});


const jsText = document.getElementById('jsText');
const textChangeForm = document.getElementById('textChangeForm');

const colorInput = document.getElementById('colorInput');
const sizeInput = document.getElementById('sizeInput');
const backgroundInput = document.getElementById('backgroundInput');

const jsTextColor = document.getElementById('jsTextColor');
const jsTextSize = document.getElementById('jsTextSize');
const jsBackgroundColor = document.getElementById('jsBackgroundColor');

const formObject = {
    colorInput: jsTextColor,
    sizeInput: jsTextSize,
    backgroundInput: jsBackgroundColor
};

//console.dir(formObject);

jsText.addEventListener('dblclick', (e) => {
    //e.preventDefault();
    //console.log(jsTextColor.value)
    textChangeForm.style.display = 'flex'; // Fade in
    setTimeout(() => {
    textChangeForm.classList.toggle('active');
    }, 0);
    //textChangeForm.classList.toggle('active');

    setTimeout(() => {
    if(!textChangeForm.classList.contains('active')){
        textChangeForm.style.display = 'none'; // Fade in
    }
    }, 400);

})
jsTextColor.addEventListener('change', () => {
    console.log(jsTextColor.value)
    jsText.style.color = jsTextColor.value;
})
jsTextSize.addEventListener('change', (e) => {
    e.preventDefault();
    console.log(jsTextSize.value)
    jsText.style.fontSize = jsTextSize.value + "px";
})
jsBackgroundColor.addEventListener('change', () => {
    console.log(jsBackgroundColor.value)
    jsText.style.background = jsBackgroundColor.value;
})
textChangeForm.addEventListener('submit', (e) => {
    e.preventDefault();
})
colorInput.addEventListener('change', () => {
    if (colorInput.checked) {
        jsTextColor.style.display = 'block';
    } else {
        jsTextColor.style.display = 'none';
    }
})
sizeInput.addEventListener('change', () => {
    if (sizeInput.checked) {
        jsTextSize.style.display = 'block';
    } else {
        jsTextSize.style.display = 'none';
    }
})
backgroundInput.addEventListener('change', () => {
    if (backgroundInput.checked) {
        jsBackgroundColor.style.display = 'block';
    } else {
        jsBackgroundColor.style.display = 'none';
    }
})


//function Shape(x, y){
//
//}

class Shape {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    getArea() {
        return "Площадь не определена";
    }

    getPerimeter() {
        return "Периметр не определен";
    }

    static double(a){
        return a * a;
    }


}
function desc(target, key, descriptor) {
  console.log(descriptor);
  const originalMethod = descriptor.value;
  console.log("We use descriptor");

  descriptor.value = function() {
      originalMethod.apply(this, arguments);
  };

  return descriptor;
}
function logMethod(target, key, descriptor) {
  const originalMethod = descriptor.value; // Save the original method

  // Redefine the method with custom behavior
  descriptor.value = function (...args) {
    console.log(`Before ${key} is called`);
    const result = originalMethod.apply(this, args);
    console.log(`After ${key} is called`);
    return result;
  };

  return descriptor;
}
class Circle extends Shape {
    constructor(x, y, radius) {
        super(x, y);
        this._radius = radius;
    }

    get radius() {
        return this._radius;
    }

    set radius(newRadius){
        if(newRadius>0){
            this._radius = newRadius;
        }
        else{
            console.error("Negative radius");
        }
    }

    getArea() {
        console.log(this.constructor.double(this._radius));
        return Math.PI * super.constructor.double(this._radius);
    }

    getPerimeter() {
        return Math.PI * this.getDiameter();
    }

    getDiameter(){
        return this._radius * 2
    }
}

//const hasFuel = function(fn) {
//
//  return function() {
//    if (this.fuel <= 0) {
//      console.log("No fuel");
//    }
//    console.log(this);
//    return fn.call(this);
//  }
//}
//function hasFuel(target, key, descriptor) {
//console.log(descriptor);
//  const originalMethod = descriptor.value;
//
//  descriptor.value = function() {
//    if (this.fuel > 0) {
//      originalMethod.apply(this, arguments);
//    } else {
//      console.log('Fuel is empty. Refill the tank.');
//    }
//  };
//
//  return descriptor;
//}


function hasFuel(originalFunction) {
  return function() {
    console.log(`Calling ${originalFunction.name}`);
//    console.dir(originalFunction.call(this));
    if (this.fuel > 0) {
//        const result = originalFunction.call(this);
        return originalFunction.call(this);
    }
    else {
      console.log('Fuel is empty. Refill the tank.');
      result = 0;
    }
//    console.log(`${originalFunction.name} returned:`, result);
    console.log("Res " + result);
    return result;
  };
}
function Car(model, fuel){
    this.model = model;
    this.fuel = fuel;
}

const drive = function(){
    console.log(this);
    this.fuel -= 5;
    return this.fuel;
}

Car.prototype.drive = hasFuel(function(){
    //console.log(this);
    this.fuel -= 5;
    return this.fuel;
});

function Ferrari(model, fuel, topSpeed){
    Car.call(this, model, fuel, topSpeed);
    this.topSpeed = topSpeed;
}
Ferrari.prototype = Object.create(Car.prototype);

Ferrari.prototype.showOff = function() {
  console.log(`Look at my Ferrari! It can go up to ${this.topSpeed} mph.`);
};