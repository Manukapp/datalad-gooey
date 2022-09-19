# each item is a command that is allowed in the API
# the key is the command name in the Python API.
# the values are dicts with the following keys
# - exclude_parameters: set with parameter names to
#   exclude from the API

api = dict(
    clone=dict(
        exclude_parameters=set((
            'git_clone_opts',
            'reckless',
            'description',
        )),
    ),
    create=dict(
        name='Create a dataset',
        exclude_parameters=set((
            'initopts',
            'description',
            'fake_dates',
        )),
        parameter_display_names=dict(
            force='OK if target directory not empty',
            path='Create at',
            dataset='Register in dataset',
        ),
        parameter_order=dict(
            path=0,
            annex=1,
            dataset=2,
        ),
    ),
    create_sibling_gitlab=dict(
    ),
    create_sibling_gin=dict(
    ),
    create_sibling_github=dict(
    ),
    drop=dict(
    ),
    get=dict(
    ),
    push=dict(
    ),
    save=dict(
    ),
    update=dict(
    ),
)

exclude_parameters = set((
    'result_renderer',
    'return_type',
    'result_filter',
    'result_xfm',
    'on_failure',
))

parameter_display_names = dict(
    annex='Dataset with file annex',
    cfg_proc='Configuration procedure(s)',
    dataset='Dataset location',
)

dataset_api = {
    c: s for c, s in api.items()
    if c in (
        'clone', 'create', 'create_sibling_gitlab', 'create_sibling_gin',
        'create_sibling_github', 'drop', 'get', 'push', 'save', 'update'
    )
}
directory_api = {
    c: s for c, s in api.items() if c in ('clone', 'create')
}
directory_in_ds_api = {
    c: s for c, s in api.items()
    if c in ('clone', 'create', 'drop', 'get', 'push', 'save')
}
file_api = None
file_in_ds_api = {
    c: s for c, s in api.items() if c in ('save', 'get', 'drop')
}
annexed_file_api = {
    c: s for c, s in api.items()
    if c in ('drop', 'get', 'push', 'save')
}

# simplified API has no groups
api_group_order = {}
