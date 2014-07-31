({
    baseUrl: "geordi/geordi/static/scripts",
    mainConfigFile: "geordi/geordi/static/scripts/common.js",
    dir: "geordi/geordi/static/build/scripts",
    optimize: "uglify2",
    skipDirOptimize: true,
    removeCombined: true,
    fileExclusionRegExp: /^(\.|less\.js$)/,
    modules: [
        {
            name: "common"
        }
    ]
})
