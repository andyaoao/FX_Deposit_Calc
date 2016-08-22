var pg = require( 'pg' );
var promise = require( 'promise');

exports.index = function(req, res) {

   // console.log("In insert");
   // // Connect to DB
   // var conString = "postgres://postgres:0000@localhost:5432/FXData";
   // var client = new pg.Client(conString);
   // client.connect(); 

   // //Drop table if it exists
   // client.query("DROP TABLE IF EXISTS emps");

   // // Creat table and insert 2 records into it
   // client.query("CREATE TABLE IF NOT EXISTS emps(firstname varchar(64), lastname varchar(64))");
   // client.query("INSERT INTO emps(firstname, lastname) values($1, $2)", ['Tinniam', 'Ganesh']);
   // client.query("INSERT INTO emps(firstname, lastname) values($1, $2)", ['Anand', 'Karthik']);

   // // Write output
   // res.writeHead(200, {'Content-Type': 'text/plain'});
   // res.write("2 records is inserted.\n");
   // res.end();
   // console.log("Inserted 2 records");

	
  console.log("In listing records");

  // Connect to DB
  var conString = "postgres://postgres:0000@localhost:5432/FXData";
  var client = new pg.Client(conString);
  client.connect(onConnect); 
	function onConnect(err, client, done) {
	  //Err - This means something went wrong connecting to the database.
	  if (err) {
	    console.error(err);
	    process.exit(1);
	  }
	  console.log("DB connected")
	  // client.end();
	}

	// Select all rows in the table
	var query =  client.query('SELECT * FROM IntRates', function(err, result) {
		console.log(result);
	});

	query.on("row", function (row, result) {
		 result.addRow(row);
	});
	query.on("end", function (result) {
	  
	// On end JSONify and write the results to console and to HTML output
	console.log(JSON.stringify(result.rows, null, "    "));
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.write(JSON.stringify(result.rows) + "\n");
		res.end();
	});
	res.render('index', {
	  // title: 'TimeLine',
	  // results: results
});

}

exports.supply = function(req, res) {
	// console.log('in latest model');
	console.log('in supply catogory ', req.params.id);
	if(req.params.id == 0){
		Supply.
		find().
		sort( '-updated_at' ).
		exec(function(err, items) {
			if (err) {
				console.error(err);
			};
			res.json(items);
		});	
	}
	else{
		Supply.
		find({
			catogory: req.params.id
		}).
		exec(function(err, items) {
			if (err) {
				console.error(err);
			};
			res.json(items);
		});		
	}
}