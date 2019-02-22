JINJA_TEMPLATE = '''
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        .filterDiv {
            display: none;
        }
        
        .show {
            display: none;
        }
        
        .tagShow {
            display: none;
        }
        
        .extraTagShow {
            display: none;
        }
        
        .show.tagShow.extraTagShow {
            display: block;
        }
    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

<body>

    <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="index.html">
            <img src="images/workshare_nav.png" height="30" class="d-inline-block align-top" alt="Workshare"> Home
        </a>
        <a class="navbar-brand" href="qa_output.html">
            <img src="images/connect2.png" width="30" height="30" class="d-inline-block align-top" alt="Connect"> Connect
        </a>
        <a class="navbar-brand" href="alpaca_output.html">
            <img src="images/alpaca.png" width="30" height="30" class="d-inline-block align-top" alt="Transact"> Transact
        </a>
        <a class="navbar-brand" href="#">
            <img src="images/deltaview.png" width="30" height="30" class="d-inline-block align-top" alt="DeltaView"> DeltaView
        </a>
        <a class="navbar-brand" href="#">
            <img src="images/risk_analytics.png" width="30" height="30" class="d-inline-block align-top" alt="Risk Analytics"> Risk Analytics
        </a>
    </nav>
    <div id="filterSection">
        <div id="myBtnContainer" style="margin-top:15px;">
            <div style="float:left;margin-right:60px;margin-left:22px;">
                <button class="btn btn-outline-dark active" onclick="filterSelection('all')"> Show all</button>
                <button class="btn btn-outline-dark" onclick="filterSelection('web')"> FE</button>
                <button class="btn btn-outline-dark" onclick="filterSelection('api')"> API</button>
                <button class="btn btn-outline-dark" onclick="filterSelection('events')"> EVENTS</button>
            </div>
        </div>
        <div class="form-inline" id="searchForm" style="margin-top:15px;">
            <div>
                <input class="form-control" id="submitTag" type="search" placeholder="Search by tag" aria-label="Search">
                <button class="btn btn-dark" onclick="tagFilterSelection()" type="button">Search</button>
                <span class="input-group-btn">
                        <button class="btn btn-outline-dark" onclick="tagFilterSelection('clear')" style="margin-right:60px;" type="button">Clear</button>
                    </span>
            </div>
            <span id="addfilter" class="btn btn-outline-dark" onclick="showExtraFilter()">Add extra filter</span>
            <div id="extrafilter" style="display:none;">
                <input class="form-control" id="submitTag2" type="search" placeholder="Search by additional tag" aria-label="Search">
                <button class="btn btn-dark my-2 my-sm-0" onclick="tagFilterSelection('searchbox', 'extraTagShow')" type="button">Search</button>
                <span class="input-group-btn">
                        <button class="btn btn-outline-dark" onclick="tagFilterSelection('clear', 'extraTagShow')" style="margin-right:60px;" type="button">Clear</button>
                    </span>
            </div>
            <span id="removefilter" class="btn btn-outline-dark" style="display:none;" onclick="hideExtraFilter();">Remove extra filter</span>
        </div>
        <div style="margin-top:15px;">
            <span id="filter-summary" style="margin-left:375px;" align="left"><b id=numberresults></b> results shown. Searching by: <b id=categoryfilterapplied></b> <b id=tagfilterapplied></b> <b id=extratagfilterapplied></b></span>
            <span id="last-execution" style="margin-right:20px;float:right;">Last generated on <em>{{last_execution}}</em></span>
        </div>
    </div>
    <div id="suite-accordion">
        <ul class="list-group list-group-flush" style="margin-top:15px;">
            {% for test_suite in test_suites %} {% set suite_loop = loop %}
            <div class="filterDiv{% for tag in test_suite.setting_table.force_tags.value %} {{tag.lower()}}{% endfor %} show tagShow extraTagShow" style="background-color:#F2F2F2;">
                <li class="list-group-item" style="padding: .25rem 1.25rem;">
                    <div class="card">
                        <div class="card-header" id="suite-heading-{{suite_loop.index}}">
                            <h5 class="mb-0">
                            <button class="btn btn-link collapsed" style="color:Black;font-family:Lato;font-size:20px" data-toggle="collapse" data-target="#collapse-{{suite_loop.index}}" aria-expanded="false" aria-controls="collapse-{{suite_loop.index}}">
                              {{ test_suite.name }}
                            </button>
                                {% for tag in test_suite.setting_table.force_tags.value %}
                                    <span class="btn badge badge-pill badge-secondary" onclick="tagFilterSelection('{{tag}}')";>{{tag}}</span>
                                {% endfor %}
                          </h5>
                        </div>

                        <div id="collapse-{{suite_loop.index}}" class="collapse" aria-labelledby="suite-heading-{{suite_loop.index}}">
                            <div class="card-body" id="test-accordion">
                                <ol class="list-group list-group-flush">
                                    {% for test_case in test_suite.testcase_table %}
                                    <li class="list-group-item" style="border:none;padding: .25rem .75rem;">
                                        <div class="card">
                                            <div class="card-header" id="test-heading-{{suite_loop.index}}-{{loop.index}}">
                                                <h5 class="mb-0">
                                                <button class="btn btn-link collapsed in" style="color:Black;font-size:19px;" data-toggle="collapse" data-target="#test-collapse-{{suite_loop.index}}-{{loop.index}}" aria-expanded="false" aria-controls="test-collapse-{{suite_loop.index}}-{{loop.index}}">
                                                  {{ test_case.name }}
                                                </button>
                                              </h5>
                                            </div>
                                            <div id="test-collapse-{{suite_loop.index}}-{{loop.index}}" class="collapse" aria-labelledby="test-heading-{{suite_loop.index}}-{{loop.index}}">
                                                <div class="card-body">
                                                    <ul class="list-group list-group-flush">
                                                        {%- for test_step in test_case.steps -%}
                                                        <div class="keyword" style="font-size:18px;">
                                                            {{- test_step.name if test_step.name is not none -}} 
                                                            {%- if test_step.args|length>0 -%}
                                                                <strong>: {{ test_step.args|join(' ') }}</strong>
                                                            {%- endif -%}
                                                        </div>                                                       
                                                        {%- endfor -%}
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    {% endfor %}
                                </ol>
                            </div>
                        </div>
                    </div>
                </li>
            </div>
            {% endfor %}
        </ul>
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <script>
        showResults();

        function filterSelection(c) {
            var x, i;
            $('.filterDiv').removeClass("show");
            if (c == "all") {
                $('.filterDiv').addClass("show");
                c = "";
            } else $('.filterDiv.' + c).addClass("show");
            $("#categoryfilterapplied").html(c);
            showResults()
        }

        function showResults() {
            var matches;
            matches = $('.show.tagShow.extraTagShow').length
            $("#numberresults").html(matches);
        }

        function tagFilterSelection(filter = 'searchbox', tag = 'tagShow') {
            var id, input, filterresult;
            $('.filterDiv').removeClass(tag);
            if (filter == "clear") {
                $('.filterDiv').addClass(tag);
                if (tag == "tagShow") {
                    $("#tagfilterapplied").html("");
                } else if (tag == "extraTagShow") {
                    $("#extratagfilterapplied").html("");
                }
            } else if (filter == "searchbox") {
                if (tag == "tagShow") {
                    id = 'submitTag';
                    filterresult = "tagfilterapplied";
                } else if (tag == "extraTagShow") {
                    id = 'submitTag2';
                    filterresult = "extratagfilterapplied";
                }
                input = document.getElementById(id).value;
                $('.filterDiv.' + input).addClass(tag);
                $("#" + filterresult).html(input);
            } else {
                $('.filterDiv.' + filter).addClass("tagShow");
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
                pattern = words.join('|^').replace(/(?!\|)/, '^');
                regex = RegExp(pattern, 'gi'),
                replacement = '<' + tag + '>$&</' + tag + '>';

            return this.html(function() {
                return $(this).text().replace(regex, replacement);
            });
        };

        $('.keyword').wrapInTag({
            tag: 'strong',
            words: ['Given', 'When', 'Then', 'And']
        });

        var tagFilter = document.getElementById("searchForm");
        tagFilter.addEventListener("keydown", function(e) {
            if (e.keyCode === 13) {
                tagFilterSelection();
            }

        });

        var btnContainer = document.getElementById("myBtnContainer");
        var btns = btnContainer.getElementsByClassName("btn");
        for (var i = 0; i < btns.length; i++) {
            btns[i].addEventListener("click", function() {
                var current = document.getElementsByClassName("active");
                current[0].className = current[0].className.replace(" active", "");
                this.className += " active";
            });
        }
    </script>
</body>
</html>
'''
