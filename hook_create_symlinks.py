import os

external_path = "/srv/dealii"

symlinks = [
    # external_path + "/documentation/8.5.1",
    # external_path + "/documentation/9.0.0",
    # external_path + "/documentation/9.1.1",
    # external_path + "/documentation/9.2.0",
    # external_path + "/documentation/9.3.3",
    # external_path + "/documentation/9.4.0",
    # external_path + "/documentation/9.4.1",
    # external_path + "/documentation/9.5.0",
    # external_path + "/documentation/9.6.0",
    # external_path + "/documentation/current",
    # external_path + "/documentation/developer",
    # external_path + "/external_assets/downloads",
    # external_path + "/external_assets/fancy-index",
    # external_path + "/external_assets/performance_tests",
    # external_path + "/external_assets/regression_tests",
    # external_path + "/website-build.log",
    # "large_assets/release-papers/deal83-preprint.pdf",
    # "large_assets/release-papers/deal84-preprint.pdf",
    # "large_assets/release-papers/deal85-preprint.pdf",
    # "large_assets/release-papers/deal90-preprint.pdf",
    # "large_assets/release-papers/deal91-preprint.pdf",
    # "large_assets/release-papers/deal92-preprint.pdf",
    # "large_assets/release-papers/deal93-preprint.pdf",
    # "large_assets/release-papers/deal94-preprint.pdf",
    # "large_assets/release-papers/deal95-preprint.pdf",
    # "large_assets/workshops/workshop-2010",
    # "large_assets/workshops/workshop-2012",
    # "large_assets/workshops/workshop-2013",
    # "large_assets/workshops/workshop-2015",
    # "large_assets/workshops/workshop-2018",
    # "large_assets/workshops/workshop-2019",
    # "large_assets/workshops/workshop-2020",
    # "large_assets/workshops/workshop-2021",
    # "large_assets/workshops/workshop-2023",
    # "large_assets/workshops/workshop-2024",
    # "large_assets/images",
]


def on_post_build(**kwargs):
    "Post-build actions"

    config = kwargs['config']
    site_dir = config['site_dir']

    print("Putting symlinks in place")
    print("site_dir = ", site_dir)

    for src in symlinks:
        dst = os.path.basename(src)
        dst = os.path.join(site_dir, dst)

        if os.path.lexists(dst):
            if not os.path.islink(dst):
                raise Exception("Symlink target »" + dst +
                                "« exists and is not a symlink")
            os.remove(dst)

        print(dst, " -> ", src)
        os.symlink(src, dst)
