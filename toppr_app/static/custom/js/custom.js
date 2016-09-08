//Function for converting records to text
function write_battle_record(data){

    var record_text = "The "+ data.name + " began on the year " + data.year +
        ". King " + data.attacker_king + " launched a " + data.battle_type +
        " against the King " + data.defender_king + ". It was a momentous battle" +
        " with attcking soldiers of strength " + data.attacker_size +
        " fighting against defenders of strength " + data.defender_size + ". " +
        data.attacker_commander + " led the army against " + data.defender_commander +
        ". The battle was fought on " + data.location + " in " + data.region +
        ". The attackers scored a " + data.attacker_outcome + " against the defenders.";
    return record_text;
}

//Fetch all battle data
if($('#battle-list-all').length){
    $.ajax({
        url: '/api/list',
        dataType: 'json',
        success: function(data) {
            var no_rec = "<h4>A total of " + data.length +" battle records were found.</h4>";
            $('#battle-list-all-body').append(no_rec);
            for (i=0; i < data.length; i++){
                var rec_no = "<p><b>Battle Record # " + (i+1) + "</b></p>";
                $('#battle-list-all-body').append(rec_no);
                record_text = write_battle_record(data[i]);
                $('#battle-list-all-body').append("<p>"+record_text+"</p>");
            }},
        error: function(){
            console.log("Error");
        }
    });
};

//Fetch data by number
function fetch_battle_data_no() {
    $.ajax({
        url: '/api/list/' + $('#battle-number').val(),
        dataType: 'json',
        success: function(data) {
            $('#single-battle-record').html('');
            var no_rec = "<h4>" + data.length +" battle record were found.</h4>";
            $('#single-battle-record').append(no_rec);
            record_text = write_battle_record(data[0]);
            $('#single-battle-record').append("<p>"+record_text+"</p>");
        },
        error: function(){
            console.log("Error");
        }
    });
}


//Function for searching records
function search_battle_record(){
    var battle_name = $('#battle-name').val().split(",");
    var att_king = $('#attacker-king').val().split(",");
    var def_king = $('#defender-king').val().split(",");
    var battle_type = $('#battle-type').val().split(",");
    var battle_loc = $('#battle-location').val().split(",");
    var final_string = '';
    for(i=0; i<battle_name.length;i++){
        final_string += ("name="+battle_name[i]+"&")
    };
    for(i=0; i<att_king.length;i++){
        final_string += ("attacker_king="+att_king[i]+"&")
    };
    for(i=0; i<def_king.length;i++){
        final_string += ("defender_king="+def_king[i]+"&")
    };
    for(i=0; i<battle_type.length;i++){
        final_string += ("battle_type="+battle_type[i]+"&")
    };
    for(i=0; i<battle_loc.length;i++){
        final_string += ("location="+battle_loc[i]+"&")
    };
    $.ajax({
        url: '/api/search?' + final_string,
        dataType: 'json',
        success: function(data) {
            $('#search-results-data').html("<br>")
            $('#battle-name').val("");
            $('#attacker-king').val("");
            $('#defender-king').val("");
            $('#battle-type').val("");
            $('#battle-location').val("");
            var no_rec = "<h4>A total of " + data.length +" battle records were found.</h4>";
            $('#search-results-data').append(no_rec);
            for (i=0; i < data.length; i++){
                var rec_no = "<p><b>Battle Record # " + (i+1) + "</b></p>";
                $('#search-results-data').append(rec_no);
                record_text = write_battle_record(data[i]);
                $('#search-results-data').append("<p>"+record_text+"</p>");
            }},
        error: function(){
            console.log("Error");
        }
    });
}


//Function for getting the battle statistics
if($('#battle-statistics').length){
    $.ajax({
        url: '/api/stats',
        dataType: 'json',
        success: function(data) {
            console.log(data);
            var json_string = JSON.stringify(data, null, 2);
            console.log(json_string);
            $('#battle-statistics').append(json_string);
            },
        error: function(){
            console.log("Error");
        }
    });
};
