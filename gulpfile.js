const { series, parallel } = require("gulp");

// function defaultTask(cb) {
//     // place code for your default task here
//     cb();
//   }
  
function scssTask(){    
    return src(files.scssPath) //loading directory of source files
        .pipe(sourcemaps.init()) 
        .pipe(sass()) //compiles all scss files into one css file
        .pipe(postcss([ autoprefixer(), cssnano() ])) //autoprefixer adds vendor prefixes to css, cssnano minifies code
        .pipe(sourcemaps.write('.')) //creates sourcemap file in same directory
        .pipe(dest('dist') //tells gulp to put final css file in dist directory
    );
}  

function jsTask(){
    return src([files.jsPath]) //loads files from jspath
        .pipe(concat('all.js')) //concats all js files into one 
        .pipe(uglify()) //uglifies/minifies code
        .pipe(dest('dist') //moves final file into dist directory
    );
}

//cashbust task, forces server to re-deploy when css and js are updated

var cbString = new Date().getTime();
function cacheBustTask(){
    return src(['index.html'])
        .pipe(replace(/cb=\d+/, 'cb=' + cbString))
        .pipe(dest('.'));
}

//watch task, runs continuously so you don't have to use 'gulp' command after every change

function watchTask(){
    watch(
        [files.scssPath, files.jsPath],
        parallel(scssTask, jsTask)
    );
}

exports.default = series(parallel(scssTask, jsTask), watchTask)