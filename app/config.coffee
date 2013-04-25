exports.config =
  # See http://brunch.readthedocs.org/en/latest/config.html for documentation.
  paths:
    public: '../static/'

  files:
    javascripts:
      joinTo:
        'js/app.js': /^app(\/|\\)(?!templates)/
        'js/vendor.js': /^vendor/
        'test/js/test.js': /^test[\\/](?!vendor)/
        'test/js/test-vendor.js': /^test[\\/](?=vendor)/
      order:
        # Files in `vendor` directories are compiled before other files
        # even if they aren't specified in order.before.
        before: [
          #'vendor/scripts/console-helper.js',
          #'vendor/scripts/jquery-1.8.2.js',
          #'vendor/scripts/underscore-1.4.0.js',
          #'vendor/scripts/backbone-0.9.2.js'
        ]

    stylesheets:
      defaultExtension: 'scss'
      joinTo:
        'css/app.css': /^(app|vendor)/
        'test/css/test.css': /^test/
      #order:
        #before: ['vendor/styles/normalize-1.0.1.css']
        #after: ['vendor/styles/helpers.css']

    templates:
      joinTo: 'js/app.js'
