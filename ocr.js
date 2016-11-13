var ocrDemo = {
    
    CANVAS_WIDTH:     200,
    TRANSLATED_WIDTH: 20,
    PIXEL_WIDTH:      10,   // 200/20=10
    BATCH_SIZE:       1,
    
    // server-side port
    PORT: "9000",
    HOST: "http://localhost",

    // color
    BLACK: "#000000",
    BLUE: "#0000ff",

    // client-side training data set
    trainArray: [],
    trainingRequestCount: 0,

    onLoadFunction: function(){
	this.resetCanvas();
    },
    
    resetCanvas: function(){
	var canvas = document.getElementById('canvas');
	var ctx = canvas.getContext('2d');
	this.data = [];
	ctx.fillStyle = this.BLACK;
	ctx.fillRect(0, 0, this.CANVAS_WIDTH, this.CANVAS_WIDTH);
	var matrixSize = 400;
	while(matrixSize--)
	    this.data.push(0);
	this.drawGrid(ctx);

    }



}





