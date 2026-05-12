# Sublime Text 3 support for [Hexa](https://github.com/hexalang)

[![Join the Gitter chat](https://badges.gitter.im/hexalang/hexalang.svg)](https://gitter.im/hexalang/SublimeText?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

![Screenshot](screenshot.png?raw=true)

### Install

<https://packagecontrol.io/packages/Hexa>

#### Language Server

You need to install `LSP` package if it's not present in your Sublime Text installation.

Install [the Hexa itself](https://hexalang.github.io/).

Restart Sublime.

### Use with [Sublime Merge](https://www.sublimemerge.com/)

Open `Preferences -> Browse Packages...` and copy [syntax file](https://github.com/hexalang/hexa-sublime-bundle/blob/master/Hexa.tmLanguage) into `User` subfolder of `Packages`, restart Sublime Merge

#### Supported features

- Syntax highlight
- Syntax errors (via compiler's LSP)
- Build systems
- Code navigation
- Snippets
