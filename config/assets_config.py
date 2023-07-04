from flask_assets import Environment, Bundle

def create_bundle(input_file, output_file=None):

    if output_file is None:
        output_file = input_file

    bundle = Bundle(
        f'scss/{input_file}.scss',
        filters=['libsass'],
        output=f'dist/css/{output_file}.css',
        depends='scss/*.scss'
    )

    return bundle

def configure_assets(app):
    assets = Environment(app)

    bundle_names = ['base_css', 'index_css']
    bundles = {name: create_bundle(name.split('_')[0]) for name in bundle_names}

    for bundle_name, bundle_obj in bundles.items():
        assets.register(bundle_name, bundle_obj)
        bundle_obj.build()
