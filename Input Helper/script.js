document.addEventListener("DOMContentLoaded", () => {
    const jsonTypeSelect = document.getElementById("jsonType");
    jsonTypeSelect.addEventListener("change", () => {
        generateForm(jsonConfigurations[jsonTypeSelect.value]);
    });

    // Initialize form and output JSON on page load
    generateForm(jsonConfigurations[jsonTypeSelect.value]);
});

function generateForm(data, parentElement = document.getElementById('formContainer')) {
    parentElement.innerHTML = '';
    createFormElements(data, parentElement, data);
    updateJSONOutput(data); // Ensure JSON preview updates immediately
}
function createFormElements(data, parentElement, rootObject) {
    for (let key in data) {
        const value = data[key];
        const wrapper = document.createElement('div');
        wrapper.style.marginBottom = '10px';
        wrapper.style.borderBottom = '1px solid #ccc'; // Light gray separator line
        wrapper.style.paddingBottom = '10px';

        let label = document.createElement('label');
        label.textContent = key;
        label.style.display = 'block';

        let description = null;
        let isRequired = false;

        // If it's an object with "default", treat it as a configurable value
        if (typeof value === 'object' && value !== null && 'default' in value) {
            const finalValue = value.default;
            description = value.description || "";
            isRequired = value.required || false;
            const inputType = value.type || "checkbox"; // Default to checkbox if type isn't given

            // Apply 'required' style
            if (isRequired) {
                label.style.fontWeight = 'bold';
                label.style.color = 'red';
            }

            // Ensure name and description appear at the top
            wrapper.appendChild(label);
            if (description) {
                const descElement = document.createElement('small');
                descElement.textContent = description;
                descElement.style.display = 'block';
                descElement.style.color = '#666';
                wrapper.appendChild(descElement);
            }

            let inputContainer = document.createElement('div');

            // Handling different types
            if (typeof finalValue === 'boolean') {
                let input = document.createElement('input');
                input.type = 'checkbox';
                input.checked = finalValue;
                input.style.marginRight = '5px';

                input.addEventListener('change', () => {
                    data[key].default = input.checked;
                    updateJSONOutput(rootObject);
                });

                inputContainer.appendChild(input);
            } else if (typeof finalValue === 'string' || finalValue === null) {
                let input = document.createElement('input');
                input.type = 'text';
                input.value = finalValue ?? '';
                input.placeholder = finalValue === null ? 'null' : '';

                input.addEventListener('input', () => {
                    data[key].default = input.value || null;
                    updateJSONOutput(rootObject);
                });

                inputContainer.appendChild(input);
            } else if (typeof finalValue === 'number') {
                let input = document.createElement('input');
                input.type = 'number';
                input.value = finalValue;

                input.addEventListener('input', () => {
                    data[key].default = Number(input.value);
                    updateJSONOutput(rootObject);
                });

                inputContainer.appendChild(input);
            } else if (Array.isArray(finalValue)) {
                if (inputType === "checkbox") {
                    // Checkbox-based multi-selection (default behavior)
                    const checkboxContainer = document.createElement('div');
                    checkboxContainer.classList.add('checkbox-container');

                    data[key].default = Array.isArray(data[key].default) ? data[key].default : []; // Ensure it's an array

                    finalValue.forEach(optionValue => {
                        const checkboxWrapper = document.createElement('div');
                        checkboxWrapper.style.display = 'flex';
                        checkboxWrapper.style.alignItems = 'center';

                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.value = optionValue;
                        checkbox.checked = data[key].default.includes(optionValue);
                        checkbox.style.marginRight = '5px';

                        checkbox.addEventListener('change', () => {
                            if (checkbox.checked) {
                                if (!data[key].default.includes(optionValue)) {
                                    data[key].default.push(optionValue);
                                }
                            } else {
                                data[key].default = data[key].default.filter(item => item !== optionValue);
                            }
                            updateJSONOutput(rootObject);
                        });

                        const checkboxLabel = document.createElement('label');
                        checkboxLabel.textContent = optionValue;
                        checkboxWrapper.appendChild(checkbox);
                        checkboxWrapper.appendChild(checkboxLabel);
                        checkboxContainer.appendChild(checkboxWrapper);
                    });

                    inputContainer.appendChild(checkboxContainer);
                } else if (inputType === "custom") {
                    // Custom input system for dynamic values
                    const listContainer = document.createElement('div');
                    listContainer.style.marginTop = '5px';
                    listContainer.style.display = 'flex';
                    listContainer.style.flexWrap = 'wrap';
                    listContainer.style.gap = '5px';

                    const inputField = document.createElement('input');
                    inputField.type = 'text';
                    inputField.placeholder = 'Enter a value';
                    inputField.style.marginRight = '10px';

                    const addButton = document.createElement('button');
                    addButton.textContent = 'Add';
                    addButton.style.cursor = 'pointer';

                    const updateList = () => {
                        listContainer.innerHTML = '';
                        data[key].default.forEach((item, index) => {
                            const itemDiv = document.createElement('div');
                            itemDiv.style.display = 'inline-flex';
                            itemDiv.style.alignItems = 'center';
                            itemDiv.style.background = '#f0f0f0';
                            itemDiv.style.padding = '5px 10px';
                            itemDiv.style.borderRadius = '15px';

                            const itemText = document.createElement('span');
                            itemText.textContent = item;
                            itemText.style.marginRight = '10px';

                            const removeButton = document.createElement('button');
                            removeButton.textContent = '❌';
                            removeButton.style.cursor = 'pointer';
                            removeButton.style.border = 'none';
                            removeButton.style.background = 'none';
                            removeButton.style.color = 'red';
                            removeButton.style.fontSize = '14px';

                            removeButton.addEventListener('click', () => {
                                data[key].default.splice(index, 1);
                                updateList();
                                updateJSONOutput(rootObject);
                            });

                            itemDiv.appendChild(itemText);
                            itemDiv.appendChild(removeButton);
                            listContainer.appendChild(itemDiv);
                        });
                    };

                    addButton.addEventListener('click', () => {
                        const newValue = inputField.value.trim();
                        if (newValue && !data[key].default.includes(newValue)) {
                            data[key].default.push(newValue);
                            inputField.value = '';
                            updateList();
                            updateJSONOutput(rootObject);
                        }
                    });

                    inputContainer.appendChild(inputField);
                    inputContainer.appendChild(addButton);
                    inputContainer.appendChild(listContainer);
                    updateList(); // Initialize list display
                }
            }

            wrapper.appendChild(inputContainer);
        } else if (typeof value === 'object' && value !== null) {
            // Nested section
            const container = document.createElement('div');
            container.classList.add('nested-section');
        
            const separator = document.createElement('hr');
            separator.classList.add('nested-separator');
        
            parentElement.appendChild(separator); // Adds a divider before the section
            parentElement.appendChild(label);
            parentElement.appendChild(container);
            
            createFormElements(value, container, rootObject);
            continue;
        }
        
        

        parentElement.appendChild(wrapper);
    }
}



function cleanData(obj) {
    if (typeof obj !== 'object' || obj === null) return obj;

    if (obj.hasOwnProperty("default") && Array.isArray(obj.default)) {
        return [...obj.default]; // Ensure it outputs only the array
    }

    if ('default' in obj && typeof obj.default !== 'object') {
        return obj.default; // Extract only the value
    }

    if ('default' in obj) {
        return obj.default === null ? null : obj.default; // Preserve null values
    }

    const cleanObj = {};
    for (let key in obj) {
        cleanObj[key] = cleanData(obj[key]);
    }
    return cleanObj;
}

function updateJSONOutput(rootObject) {

    const cleanedData = cleanData(rootObject);
    document.getElementById('jsonOutput').textContent = JSON.stringify(cleanedData, null, 4);
}

function exportJSON() {
    const selectedConfig = jsonConfigurations[document.getElementById('jsonType').value];

    // Ensure exported data is cleaned
    const cleanedData = cleanData(selectedConfig);

    const jsonString = JSON.stringify(cleanedData, null, 4);
    const blob = new Blob([jsonString], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'config.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
