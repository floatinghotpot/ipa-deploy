#!/usr/bin/env node

'use strict';

var fs = require('fs'),
	path = require('path'),
    glob = require('glob'),
    minimist = require('minimist');

require('shelljs/global');

var ipa_deploy_cli = {
    deploy_ipa: function( ipa_file, extra_args ) {
        var ipa_path = path.resolve( ipa_file );
        if(! fs.existsSync(ipa_path)) {
            echo('ipa file not found: ' + ipa_path);
            return;
        }
        
        var tmp_path = './tmp';
        if(test('-d', tmp_path) ) rm('-r', tmp_path);
        mkdir( tmp_path );
        cd( tmp_path );

        exec( 'unzip "' + ipa_path + '"' );
        var payloadDir = './Payload';
        if(fs.existsSync(payloadDir)) {
            var files = fs.readdirSync( payloadDir );
            var appFound = false;
            for(var i=0; i<files.length; i++) {
                var filename = payloadDir + '/' + files[i];
                if(filename.indexOf('.app') + '.app'.length == filename.length) {
                    exec('ios-deploy -b "' + filename + '" ' + extra_args.join(' '));
                    appFound = true;
                }
            }
            if(! appFound) echo('.app not found in unzipped IPA, invalid IPA file?');
        } else {
            echo('Payload folder not found, invalid IPA file?');
        }
        
        cd('..');
        exec('rm -r "' + tmp_path + '"');
    },
    main: function( argv ) {
        var cli = argv[1];
        var args = minimist( argv.slice(2) );
        
        if(args._.length > 0) {
            this.deploy_ipa( args._[0], argv.slice(3) );
            
        } else {
            echo('Arguments missing. \n' + 
                 'Syntax: ipa-deploy <ipa file>\n' + 
                 'Example: ipa-deploy ./myapp.ipa\n');
        }
    }
};

ipa_deploy_cli.main( process.argv );

    

