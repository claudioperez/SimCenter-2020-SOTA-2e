Zotero.debug(JSON.stringify(item.relations))
    if (item.relations["dc:replaces"]){
        reference.add({
            name: 'related', 
            value: Zotero.items.get(
                item.relations["dc:replaces"]
            ).getField("citekey")
        })
    }
{
    "Item": "function (itemType) {var createArrays = ['creators', 'notes', 'tags', 'seeAlso', 'attachments'];this.itemType = itemType;for(var i=0, n=createArrays.length; i<n; i++) {this[createArrays[i]] = [];}}",
    "Collection": "function () {}",
    "_itemDone":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "getOption":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "getHiddenPref":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "loadTranslator":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "wait":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "done":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "debug": "function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "nextItem": "function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "nextCollection": "function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "setProgress": "function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "BetterBibTeX":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "Utilities": "function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "isBookmarklet": false,
    "isConnector": false,
    "isServer": false,
    "parentTranslator": null,
    "write":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }",
    "setCharacterSet":"function () {\n var args = passAsFirstArgument ? [passAsFirstArgument] : [];\n for (var i = 0; i < arguments.length; i++) {\n args.push(arguments[i]);\n }\n\n return fn.apply(object, args);\n }"
}
