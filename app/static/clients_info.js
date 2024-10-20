/*
This file contains JavaScript functions related to active and old
prescriptions and the corresponding buttons.
*/

// Button styles based on each page type
PRESCRIPTS_STYLE = "border-left: 10px solid #FF7F7F;\
                background-color: #ffb6b6;\
                box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);\
                height: 74px;\
                margin: 20px 0px;\
                padding-left: 10px; \
                display: flex-inline;" ;

OLD_PRESCRIPTS_STYLE = "border-left: 10px solid #B18793;\
                background-color: #c9abb4;\
                box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);\
                height: 74px;\
                margin: 20px 0px;\
                padding-left: 10px; \
                display: flex-inline;" ;

PRESCRIPTS = "prescript"

function show_items() {
    /* 
    Creates buttons for all the items on screen. 
    If search == INVENTORY, expects data == 
    [[drug_name, din, usage, dosage, quantity], ...]. 
    If search == CLIENTS, expects data == 
    [[full_name, birth_date, phone_number, active_prescriptions], ...]
    */
    // For each item in the data passed by Flask...
    num_items = data[0].length;
    for (i = 0; i < num_items; i++) {
        // Create a button
        item = document.createElement("div");
        
        // Set the correct button style.
        item.style = PRESCRIPTS_STYLE;
        // Create the text elements inside the button
        row = format_active_item(data[0][i]);
        item.appendChild(row);
    
        // Display the button on-screen
        document.getElementById("item-list").appendChild(item);
    }
    old_items = data[1].length;
    for (i = 0; i < old_items; i++) {
        // Create a button
        old_item = document.createElement("div");
        
        // Set the correct button style.
        old_item.style = OLD_PRESCRIPTS_STYLE;
        // Create the text elements inside the button
        row = format_active_item(data[1][i]);
        old_item.appendChild(row);
    
        // Display the button on-screen
        document.getElementById("old-list").appendChild(old_item);
    }
    update_status();
}

function format_active_item(data) {
    /* 
    Formats a button in 4 columns, expecting data matching:
    [full_name, birth_date, phone_number, active_prescriptions]
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
    
    // Column 2 - Next Refill Date:
    col = document.createElement("div");
    col.className = "col b-reg";
    write_text(col, "Next Refill Date:", bold=true, newline=true);
    write_text(col, data[2]);
    row.appendChild(col);

    // Column 3 - Prescribed By
    col = document.createElement("div");
    col.className = "col b-reg";
    write_text(col, "Prescribed By:", bold=true, newline=true);
    write_text(col, data[3]);
    row.appendChild(col);
   
    arr = ["Ready", "Needs Filling", "Not Ready for Renewal", "Renewal Available", "Non-Active"]

    col = document.createElement("select");
    
    col.className = "b-large";

    arr.forEach(function(optionText, index) {
        option = document.createElement("option");
        option.value = String(index+1);
        option.text = optionText;
        col.appendChild(option);
    });
    col.value = data[4];

    row.appendChild(col);
    return row;
}

function write_text(col, text, bold=false, newline=false) {
    /* Writes to the given column. */
    
    // Create the text section, bold if requested
    if (bold) { key = document.createElement("h2"); }
    else { key = document.createElement("b"); }
    
    // Update the text in the section
    key.textContent = text;    
    col.appendChild(key);
    
    // Add a break element if desired
    if (newline) {
        br = document.createElement("br");
        col.appendChild(br);    
    }
}

function update_status(){
    selectElements = document.querySelectorAll('select');

    for (let i = 0; i < selectElements.length; i++) {
       

        selectElement = selectElements[i];        
        selectElement.addEventListener('change', function() {
            if (document.getElementById('item-list').contains(this)){
                // Update the data[x][4] to reflect the selected value
                data[0][i][4] = this.value;

                if (this.value == "5") {
                    data[1].push(data[0][i])
                    data[0].splice(i, 1);

                    
                    // Remove the corresponding item from the DOM
                    itemList = document.getElementById("item-list");                
                    // Remove the specific item element
                    if (itemList.children[i]) {
                        itemList.removeChild(itemList.children[i]);
                    }

                    

                    // replace later? a little unsafe i think
                    itemList.innerHTML = '';
                    document.getElementById("old-list").innerHTML = '';
                    // refresh visual display
                    show_items()

                }

            } else if ((document.getElementById('old-list').contains(this))){
                idx = i - data[0].length;
                // Update the data[x][4] to reflect the selected value
                data[1][idx][4] = this.value;
                
                if (this.value !== "5") {

                    data[0].push(data[1][idx])

                    data[1].splice(idx, 1);

                    
                    // Remove the corresponding item from the DOM
                    itemList = document.getElementById("old-list");                
                    // Remove the specific item element
                    if (itemList.children[i]) {
                        itemList.removeChild(itemList.children[i]);
                    }

                    

                    // replace later? a little unsafe i think
                    itemList.innerHTML = '';
                    document.getElementById("item-list").innerHTML = '';
                    // refresh visual display
                    show_items()

                }

            }
        });
            
            
    }
    
}


// Load the entries from the source when the window loads in.
window.onload = (event) => { show_items(); };