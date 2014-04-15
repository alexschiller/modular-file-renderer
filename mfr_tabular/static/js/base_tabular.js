(function(){
    var columns = mfr_tabular.columns
    var rows = mfr_tabular.rows
    if(columns.length < 9){
    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
        forceFitColumns: true,
        syncColumnCellResize: true
    };
    }else{
    var options = {
        enableCellNavigation: true,
        enableColumnReorder: false,
        syncColumnCellResize: true
    };
    }
    var grid = new Slick.Grid("#mfrGrid", rows, columns, options);
})();
