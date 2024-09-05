const { src, dest, watch, series, parallel } = require("gulp");
const sass = require('gulp-sass');
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const terser = require('gulp-terser');
const browsersync = require('browser-sync').create();

//sass tasks
  
function scssTask(){    
    return src(files.scssPath) //loading directory of source files
        .pipe(sourcemaps.init()) 
        .pipe(sass()) //compiles all scss files into one css file
        .pipe(postcss([ autoprefixer(), cssnano() ])) //autoprefixer adds vendor prefixes to css, cssnano minifies code
        .pipe(sourcemaps.write('.')) //creates sourcemap file in same directory
        .pipe(dest('dist') //tells gulp to put final css file in dist directory
    );
}

//js tasks

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

//browser sync

function browsersyncServe(cb){ //initializes local browsersync server
    browsersync.init({
      server: {
        baseDir: '.'
      }    
    });
    cb();
}

function browsersyncReload(cb){ //reloads browsersync
    browsersync.reload();
    cb();
}

// watch task and update browser

function watchTask(){
    watch('*.html', browsersyncReload);
    watch(['app/**/*.scss', 'app/**/*.js'], series(scssTask, jsTask, browsersyncReload));
}

//default task that runs when you use 'gulp' command

exports.default = series(
    scssTask,
    jsTask,
    browsersyncServe,
    watchTask
);