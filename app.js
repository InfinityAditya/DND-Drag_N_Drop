Blockly.Blocks['model_train'] = {
    init: function() {
        this.appendDummyInput().appendField("Train Model");
        this.setNextStatement(true);
        this.setColour(120);
    }
};

Blockly.Blocks['model_predict'] = {
    init: function() {
        this.appendValueInput("FEATURES").setCheck("Array").appendField("Predict");
        this.setPreviousStatement(true);
        this.setColour(160);
    }
};
const workspace = Blockly.inject('blocklyDiv', {
    toolbox: document.getElementById('toolbox')
});

async function runCode() {
    const blocks = Blockly.JavaScript.workspaceToCode(workspace);
    console.log(blocks); // Logs generated code for debug
    
    try {
        const response = await fetch("http://127.0.0.1:5000/train", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({})
        });
        const data = await response.json();
        console.log(data.message);
    } catch (error) {
        console.error("Error:", error);
    }
}
