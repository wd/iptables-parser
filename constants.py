HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN" class="">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit" />
<title>Iptables</title>
<script
  src="https://code.jquery.com/jquery-3.1.1.min.js"
  integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
  crossorigin="anonymous"></script>
<style type="text/css">
table {
    border-collapse:collapse;
    position:relative;
    margin-top:1em;
    margin-bottom:1em;
    border:0;
    max-width: 80%;
}

table th,table td {
    line-height:18px;
    padding:8px 12px;
}

table td {
    text-align:left;
}

table th {
    background-color:#2A7AD2 !important;
    color:#fff;
    text-align:left;
}

table tbody th,table tbody td,table tfoot th,table tfoot td {
    border-bottom:solid 1px #eee;
}

table tbody tr:nth-child(odd) th,table tbody tr:nth-child(odd) td {
    /*background:#FAFDFE;*/
    background:#5b5b5b29;
}

a {
    margin:0;
    padding:0;
    border:0;
    font-size:100%;
    vertical-align:baseline;
    background:transparent;
    outline:none;
    color: #329ECC;
    text-decoration:none;
    border-bottom:1px solid #A1CFD4;
}

a:hover, a:focus, a:active {
    background-color:#E2EFFF;
    border-bottom:1px solid #329ECC;
}

.menu {
    position:fixed;
    float:right;
    right:0;
    top:0;
    z-index:10000;
    background-color:#f0f0f0;
    overflow: auto;
    height: 100%;
}
</style>
</head>
<body>
<div class='menu'>
<div style='float:right'>
    <span onClick='toggle_menu(this)'>close</span><span> | </span>
    <span onClick='toggle_pin(this)'>unpin</span>
</div>

<div style='float:left' class='real_menu'>
    {%- for table_name, table in tables.items() -%}
    <span><a href="#{{ table_name }}">{{ table_name }}</a></span>
    <ul>
        {%- for chain in table -%}
        {%- set chain_id = table_name + chain -%}
        <li><a href='#{{ chain_id }}'>{{ chain }}</a></li>
        {%- endfor -%}
    </ul>
    {% endfor %}
</div>

</div>

<div class="tbl">
{% for table_name, table in tables.items() -%}
<h2 id="{{ table_name }}">{{ table_name }}</h2>
{%- for chain in table -%}
{%- set policy = table[chain]["policy"] -%}
{%- set current_chain_id = table_name + chain -%}
<table>
    <tr><th>No.</th><th id="{{ current_chain_id }}">{{ chain }} {%- if policy -%}({{ policy }}){%- endif -%}</th><th>Target</th></tr>
    {%- set rules = table[chain]["rules"] -%}
    {%- for rule in rules -%}
    {%- set target_chain_id = table_name + rule[1] -%}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{ rule[0] }}</td>
        <td><a href="#{{ target_chain_id }}">{{ rule[1] }}</a></td>
    </tr>
    {% endfor %}
</table>
{% endfor %}
{% endfor %}
</div>

</body>
<script type = "text/javascript">
    function toggle_menu(me) {
        $(".menu .real_menu").toggle();
        if ( $(me).text() == 'close' ) {
            $(me).text('open');
        } else{
            $(me).text('close');
        }
    }

    function toggle_pin(me) {
        if ( $(me).text() == 'unpin' ) {
            $(me).text('pin');
            $(".menu").css('position', 'absolute');
        } else{
            $(me).text('unpin');
            $(".menu").css('position', 'fixed');
        }
    }

    $('a').click(function() {
        var arr = this.href.split('#');
        var id = arr[arr.length-1];
        var par = $(document.getElementById(id)).parent();
        par.fadeOut();
        par.fadeIn();
    });
</script>
</html>
'''
