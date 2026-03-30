# -*- coding: utf-8 -*-

from argparse import Namespace


def weld_inspector_ptv3_main(args: Namespace) -> None:
    assert isinstance(args.opts, list)

    # [IMPORTANT]
    # Do not change the import order!
    from cvpm.apps.weld_inspector_ptv3.app import WeldInspectorPtv3Application

    app = WeldInspectorPtv3Application()
    app.start()
