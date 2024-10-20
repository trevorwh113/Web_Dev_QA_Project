/*
This file contains JavaScript functions related to active and old
prescriptions and the corresponding buttons.
*/

// Item styles based on each page type

// Active Prescription Style
PRESCRIPTS_STYLE = "border-left: 10px solid #FF7F7F;\
                background-color: #ffb6b6;\
                box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);\
                height: 74px;\
                margin: 20px 0px;\
                padding-left: 10px; \
                display: flex-inline;" ;

// Inactive Prescription Style
OLD_PRESCRIPTS_STYLE = "border-left: 10px solid #B18793;\
                background-color: #c9abb4;\
                box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);\
                height: 74px;\
                margin: 20px 0px;\
                padding-left: 10px; \
                display: flex-inline;" ;


function show_items() {
    /* 
    This function takes in `data` which is an array of 2 arrays 
    which is passed through by flask, and populates two sections 
    on the page. Active items are displayed in "item-list", and inactive
    items are stored in "old-list".

    It also checks if any of the status' have been changed.
    */

    // For each item in the data for list 1 (active items) passed by Flask...
    num_items = data[0].length;
    for (i = 0; i < num_items; i++) {
        // Create an iten
        item = document.createElement("div");
        
        // Set the correct item style.
        item.style = PRESCRIPTS_STYLE;

        // Create the text elements inside the item
        row = format_active_item(data[0][i]);
        item.appendChild(row);
    
        // Display the item on-screen
        document.getElementById("item-list").appendChild(item);
    }

    // For each item in the data for list 2 (old items) passed by Flask...
    old_items = data[1].length;
    for (i = 0; i < old_items; i++) {
        // Create an item
        old_item = document.createElement("div");
        
        // Set the correct item style.
        old_item.style = OLD_PRESCRIPTS_STYLE;

        // Create the text elements inside the item
        row = format_active_item(data[1][i]);
        old_item.appendChild(row);
    
        // Display the item on-screen
        document.getElementById("old-list").appendChild(old_item);
    }
    update_status();
}

function format_active_item(data) {
    /* 
    Formats a button in 5 columns, expecting data matching:
    [drug_name, DIN, next_refill_date, prescribed_by, status]
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
   
    // Column 4 - Status
    // Generates a new select element with the options from the array
    arr = ["Ready", "Needs Filling", "Not Ready for Renewal", "Renewal Available", "Non-Active"]
    col = document.createElement("select");
    col.className = "b-large";
    arr.forEach(function(optionText, index) {
        option = document.createElement("option");
        option.value = String(index+1);
        option.text = optionText;
        col.appendChild(option);
    });

    // Selects an option to display automatically based on the status specified in data
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
/*
Continually checks if any of the select options have been changed, 
and if so will update the data passed through from flask to relfect
the status change.

Additionally:
- if option 5 (non-active) is chosen and the list is in "item-list",
  then it will be moved to the other array, display moved to "old-list", and will
  visually update the lists on the page.
- if any thing other than option 5 (non-active) is chosen and the list is in "old-list",
  then it will be moved to the other array, display moved to "item-list", and will
  visually update the lists on the page.
*/
    // grabs all select elements on the page
    selectElements = document.querySelectorAll('select');

    // loops through every element.. 
    for (let i = 0; i < selectElements.length; i++) {
        selectElement = selectElements[i];
        // listens to see if the select element is being changed
        selectElement.addEventListener('change', function() {
            // if in active list
            if (document.getElementById('item-list').contains(this)){
                // Update the data[x][4] to reflect the selected value
                data[0][i][4] = this.value;
                
                // if non-active is chosen
                if (this.value == "5") {

                    // switch it to the other data list
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
            
            // if in old list
            } else if ((document.getElementById('old-list').contains(this))){
                idx = i - data[0].length;
                // Update the data[x][4] to reflect the selected value
                data[1][idx][4] = this.value;
                
                // if anything other than non-active is chosen
                if (this.value !== "5") {

                    // switch it to the other data list
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