$(document).ready(function () {
    var filterCount = 0;
    var hasFilter = false;

    $("#mySearchTerm ").on("keyup ", {
        passive: true
    }, function () {
        filterCount = 0;

        var searchTerm = $(this).val().toLowerCase();

        rowCount = 0;

        $("#myTable tr:has(td)").filter(function () {
            rowCount++;
            if (rowCount > 1 && $(this).text().toLowerCase().indexOf(searchTerm) > -1) {
                hasFilter = true;
                filterCount++;
            };


            $(this).toggle($(this).text().toLowerCase().indexOf(searchTerm) > -1) || rowCount == 1

        })
            ;

        if (hasFilter && filterCount == 0) {
            $("#filterResult ").html("<em>No matches for \"" + searchTerm + "\"</em>");
        } else if (filterCount == 1) {
            $("#filterResult").html(" <em>" + filterCount + " matches for \"" + searchTerm + "\"</em>");
        } else if (filterCount > 1) {
            $("#filterResult").html("<em>" + filterCount + " matches for \"" + searchTerm + "\"</em>");
        }
    });
});
