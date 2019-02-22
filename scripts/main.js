<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script>

    showResults();

    function filterSelection(c) {
        var x, i;
        $('.filterDiv').removeClass("show");
        if (c == "all") {$('.filterDiv').addClass("show"); c="";}
        else $('.filterDiv.'+c).addClass("show");
        $("#categoryfilterapplied").html(c);
        showResults()
    }

    function showResults(){
        var matches;
        matches = $('.show.tagShow.extraTagShow').length
        $("#numberresults").html(matches);
    }

    function tagFilterSelection(filter = 'searchbox', tag = 'tagShow') {
        var id, input, filterresult;
        $('.filterDiv').removeClass(tag);
        if (filter == "clear") {
            $('.filterDiv').addClass(tag);
            if (tag == "tagShow") {$("#tagfilterapplied").html("");}
            else if (tag == "extraTagShow") {$("#extratagfilterapplied").html("");}
        }
        else if (filter == "searchbox") {
            if (tag == "tagShow") {
                id = 'submitTag';
                filterresult = "tagfilterapplied";
            }
            else if (tag == "extraTagShow") {
                id = 'submitTag2';
                filterresult = "extratagfilterapplied";
            }
            input = document.getElementById(id).value;
            $('.filterDiv.'+input).addClass(tag);
            $("#"+filterresult).html(input);
        }
        else {
            $('.filterDiv.'+filter).addClass("tagShow");
            $("#tagfilterapplied").html(filter);
            document.getElementById('tagfilterapplied').innerHTML = filter;
        }

        $("#submitTag").val("");
        $("#submitTag2").val("");
        showResults()
    }

    function showExtraFilter() {
        document.getElementById("addfilter").style.display = "none";
        document.getElementById("extrafilter").style.display = "block";
        document.getElementById("removefilter").style.display = "block";
    }

    function hideExtraFilter() {
        document.getElementById("removefilter").style.display = "none";
        document.getElementById("extrafilter").style.display = "none";
        document.getElementById("addfilter").style.display = "block";
        tagFilterSelection('clear', 'extraTagShow')
    }

    $.fn.wrapInTag = function(opts) {
      var tag = opts.tag || 'strong',
          words = opts.words || [],
          regex = RegExp(words.join('|'), 'gi'),
          replacement = '<'+ tag +'>$&</'+ tag +'>';

      return this.html(function() {
        return $(this).text().replace(regex, replacement);
      });
    };

    $('.keyword').wrapInTag({
      tag: 'strong',
      words: ['Given', 'When', 'Then', 'And']
    });

    var tagFilter = document.getElementById("searchForm");
    tagFilter.addEventListener("keydown", function (e) {
        if (e.keyCode === 13) {
            tagFilterSelection();
        }

    });

    var btnContainer = document.getElementById("myBtnContainer");
    var btns = btnContainer.getElementsByClassName("btn");
    for (var i = 0; i < btns.length; i++) {
      btns[i].addEventListener("click", function(){
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
      });
    }

</script>