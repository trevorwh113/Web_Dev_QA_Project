/*
This file contains JavaScript functions related to search functionality
and the corresponding buttons.
*/

BUTTON_STYLE = "margin-left: 20px; \
                margin-up: 10px; \
                padding: 5px; \
                height: 80px; \
                width: 90%; \
                background-color: #F0F7F9; \
                border-color: transparent; \
                text-align: left;";


function show_items() {
    /* Creates buttons for all the items on screen. */
    // For each item in the data passed by Flask...
    num_buttons = data.length;
    for (i = 0; i < num_buttons; i++) {
        
        // Create a button
        button = document.createElement("button");
        button.style = BUTTON_STYLE;
        
        // Create the decorative line
        line = document.createElement("i");
        line.className = "line";
        button.append(line);

        // Create the text elements inside the button
        row = format_inventory_button(data[i])
        button.appendChild(row)

        // Set the onclick event to bring you to the right page
        button.id = data[i][1];
        button.onclick = function() {
            window.location.href="/inventory/"+this.id
        }            
        
        // Display the button on-screen
        document.getElementById("button-list").appendChild(button);
    }
}

function format_inventory_button(data) {
    /* 
    Formats a button in 4 columns, expecting data matching:
    [drug_name, din, usage, dosage, quantity]
    */
    
    // Creates a row element
    row = document.createElement("div");
    row.className = "row";

    // Column 0 - Drug Name
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, "Drug Name:", bold=true, newline=true);
    write_text(col, data[0]);
    row.appendChild(col);

    // Column 1 - DIN
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, "DIN:", bold=true, newline=true);
    write_text(col, data[1]);
    row.appendChild(col);

    // Column 2 - Usage
    col = document.createElement("div");
    col.className = "col b-reg";
    write_text(col, data[2]);
    row.appendChild(col);

    // Column 3 - Dosage
    col = document.createElement("div");
    col.className = "col b-reg";
    write_text(col, data[3]);
    row.appendChild(col);
    
    // Column 4 - Quantity
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, String(data[4]) + " units");
    row.appendChild(col);

    return row;
}

function write_text(col, text, bold=false, newline=false) {
    /* Writes to the given column. */
    
    // Create the text section, bold if requested
    if (bold) { key = document.createElement("b"); }
    else { key = document.createElement("p"); }
    
    // Update the text in the section
    key.textContent = text;    
    col.appendChild(key);
    
    // Add a break element if desired
    if (newline) {
        br = document.createElement("br");
        col.appendChild(br);    
    }
}

// Load the entries from the source when the window loads in.
window.onload = show_items;