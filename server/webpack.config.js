var webpack = require('webpack');

module.exports = {
	entry: './scripts/main.ts',
	output: {
		filename: '[name].bundle.js'
	},
	resolve: {
		extensions: ['', '.ts', '.js']
	},
	module: {
		loaders: [
			{
				test: /\.ts$/,
				loader: 'ts-loader'
			}
		]
	}
};