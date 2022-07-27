function setup() {
	createCanvas(1000, 1000);
	noFill()
}

function draw() {
	
	background(240,20);
	
	strokeWeight(10)
	translate(width/2, height/2)
	
	push()
	blendMode(DARKEST);
	for(let j=0; j<TWO_PI; j+=TWO_PI/15) {
		stroke("#fa7a61")
		push()
		rotate(j)
		beginShape()
		for(let i=0; i<width/3; i+=5) {
			let ypos = sin((frameCount/2+i*0.2)/12)*50
			curveVertex(i, ypos)
		}
		endShape()
		pop()
	}
	
	for(let j=0; j<TWO_PI; j+=TWO_PI/15) {
		stroke("#93c3f1")
		push()
		rotate(j)
		beginShape()
		for(let i=0; i<width/3; i+=5) {
			let ypos = cos((frameCount/2+i*0.2)/12)*50
			curveVertex(i, ypos)
		}
		endShape()
		pop()
	}
	
	for(let j=0; j<TWO_PI; j+=TWO_PI/15) {
		stroke("#ffc145")
		push()
		rotate(j)
		beginShape()
		for(let i=0; i<width/3; i+=5) {
			let ypos = -cos((frameCount/2+i*0.2)/12)*50
			curveVertex(i, ypos)
		}
		endShape()
		pop()
	}
	pop()
	
	push()
	noStroke()
	fill(240)
	
	pop()
	
}

