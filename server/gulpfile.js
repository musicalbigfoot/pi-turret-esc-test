// Set the URL of the site here:
var PROXY_URL = "http://10.0.0.160:8080";

var gulp = require('gulp');
var sass = require('gulp-sass');
var gutil = require('gulp-util');
var plumber = require('gulp-plumber');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');
var browsersync = require('browser-sync');
var webpack = require('webpack-stream');


gulp.task('default', function() {
	browsersync({
		port: 3000,
		proxy: PROXY_URL,
		open: false
	});

	gulp.watch(['./styles/**/*.scss'], ['build:scss']);

	gulp.watch(['./scripts/**/*.ts'], ['build:ts']);
});


gulp.task('build:ts', function() {
	gulp.src('./main.ts')
		.pipe(plumber({
			errorHandler: onError
		}))
		.pipe(webpack( require('./webpack.config.js') ))
		.pipe(browsersync.stream())
		.pipe(gulp.dest('./assets/js/'));
});


gulp.task('build:scss', function() {
	gulp.src([
			'./styles/**/*.scss'
		])
		.pipe(sourcemaps.init())
		.pipe(plumber({
			errorHandler: onError
		}))
		.pipe(sass({
			style: 'compressed'
		}).on('error', sass.logError))
		.pipe(autoprefixer())
		.pipe(sourcemaps.write('./maps/'))
		.pipe(browsersync.stream())
		.pipe(gulp.dest('./assets/css/'));
});


var onError = function(err) {
	gutil.log(gutil.colors.red(err));
};