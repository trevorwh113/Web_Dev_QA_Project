/*
This file contains JavaScript functions related to search functionality
and the corresponding buttons.
*/

// Button styles based on each page type
INVENTORY_STYLE = "margin-left: 20px; \
                margin-up: 10px; \
                padding: 5px; \
                height: 80px; \
                width: 90%; \
                background-color: #F0F7F9; \
                border-color: transparent; \
                border-left: 7px solid #4B5C9E; \
                text-align: left;";

CLIENTS_STYLE = "margin-left: 20px; \
                margin-up: 10px; \
                padding: 5px; \
                height: 80px; \
                width: 90%; \
                background-color: #FFD4D4; \
                border-color: transparent; \
                border-left: 7px solid #FF8080; \
                text-align: left;";

// Type Constants for the source page.
INVENTORY = "inv"
CLIENTS = "clients"

function show_items() {
    /* 
    Creates buttons for all the items on screen. 
    If search == INVENTORY, expects data == 
    [[drug_name, din, usage, dosage, quantity], ...]. 
    If search == CLIENTS, expects data == 
    [[full_name, birth_date, phone_number, active_prescriptions], ...]
    */
    // For each item in the data passed by Flask...
    num_buttons = data.length;
    for (i = 0; i < num_buttons; i++) {
        
        // Create a button
        button = document.createElement("button");
        
        // Creating an inventory search page.
        if (search == INVENTORY) {
            // Set the correct button style.
            button.style = INVENTORY_STYLE;
        
            // Create the text elements inside the button
            row = format_inventory_button(data[i])
            button.appendChild(row)
    
            // Set the onclick event to bring you to the right page
            button.id = data[i][1];
            button.onclick = function() {
                window.location.href="/inventory/"+this.id
            }                
        }

        // Creating a client lookup page.
        else if (search == CLIENTS) {
            // Set the correct button style.
            button.style = CLIENTS_STYLE;

            // Create the text elements inside the button
            row = format_client_button(data[i])
            button.appendChild(row)
    
            // Set the onclick event to bring you to the right page
            button.id = data[i][2];
            button.onclick = function() {
                window.location.href="/prescription/"+this.id
            }                
        }
        
        // Display the button on-screen
        document.getElementById("button-list").appendChild(button);
    }
}

function format_inventory_button(data) {
    /* 
    Formats a button in 5 columns, expecting data matching:
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

function format_client_button(data) {
    /* 
    Formats a button in 4 columns, expecting data matching:
    [full_name, birth_date, phone_number, active_prescriptions]
    */
    // Creates a row element
    row = document.createElement("div");
    row.className = "row";

    // Column 0 - Full Name
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, "Client Name:", bold=true, newline=true);
    write_text(col, data[0]);
    row.appendChild(col);

    // Column 1 - Birth Date
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, "Birth Date:", bold=true, newline=true);
    write_text(col, data[1]);
    row.appendChild(col);
    
    // Column 2 - Phone Number
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, "Phone Number:", bold=true, newline=true);
    write_text(col, data[2]);
    row.appendChild(col);

    // Column 3 - Active Prescriptions
    col = document.createElement("div");
    col.className = "col b-small";
    write_text(col, "Active Prescriptions:", bold=true, newline=true);
    write_text(col, data[3]);
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