$(document).ready(function () {


    $('#myTable.sortable th').each(function (colNo) {

        $(this).hover(
            function () {
                $(this).addClass('focus');
            },
            function () {
                $(this).removeClass('focus');
            }
        );
        $(this).click(function () {

            if ($(this).is('.asc')) {
                $(this).removeClass('asc');
                $(this).addClass('desc selected');
                sortOrder = -1;
            } else {
                $(this).addClass('asc selected');
                $(this).removeClass('desc');
                sortOrder = 1;
            }
            $(this).siblings().removeClass('asc selected');
            $(this).siblings().removeClass('desc selected');
            //var arrData = $('table').find('tbody >tr:has(td)').get();
            var arrData = $('#myTable').find('tr:has(td)').get();  //this returns an array of <trs>

            sortCount = 0;

            arrData.sort(function (a, b) {

                sortCount++;

                var val1 = $(a).children('td').eq(colNo).text().toUpperCase();
                val1 = val1.replace(/,/, "");  //replace commas
                val1 = val1.replace(".", "");  //replace periods

                var val2 = $(b).children('td').eq(colNo).text().toUpperCase();
                val2 = val2.replace(/,/, "");  //replace commas
                val2 = val2.replace(".", "");  //replace periods
                //console.log("------------");
                //console.log(val1 + " / " + val2);
                sortAsDate = checkForDates(val1, val2);
                if ($.isNumeric(val1) && $.isNumeric(val2)) {
                    //console.log("sorting as number")
                    return sortOrder == 1 ? val1 - val2 : val2 - val1;
                }

                else if (sortAsDate && val1.length > 3 && val2.length > 3) {
                    //console.log("sorting as Date");
                    //console.log(d1 + " / " + d2);
                    return sortOrder == 1 ? d1.getTime() - d2.getTime() : d2.getTime() - d1.getTime()
                }

                else {
                    //console.log("sorting as string");
                    return (val1 < val2) ? -sortOrder : (val1 > val2) ? sortOrder :
                        0;
                }
            });
            appendCount = 0;
            $.each(arrData, function (index, row) {
                appendCount++;
                $('#myTable tbody').append(row);
            });
            console.log("sortcount: " + sortCount);
            console.log("appendount: " + appendCount);

        });
    });
});

function checkForDates(val1, val2) {
    bothAreDates = true;

    d1 = new Date(val1);
    d2 = new Date(val2);

    if (isNaN(d1.getTime()) || isNaN(d2.getTime())) {
        bothAreDates = false;
    }

    return bothAreDates;

}
