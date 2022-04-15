# Introduction

Parse the results of `iptables-save` to a HTML file. You can easily jump among the targets or search any keyword from `Ctrl+f`.

# Usage

Run the command below and open the `iptables.html` from your browser.

`ssh <IP> 'sudo iptables-save' | python main.py > iptables.html`

![screenshot](https://github.com/wd/iptables-parser/blob/main/screenshot.png?raw=true)
