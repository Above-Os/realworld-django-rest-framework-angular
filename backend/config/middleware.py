import re


CODER_APP_PREFIX_RE = re.compile(r"^(/@[^/]+/[^/]+/apps/[^/]+)(/.*)?$")


class StripCoderAppPrefixMiddleware:
    """
    In Coder path mode, requests may arrive as:
      /@owner/workspace.agent/apps/preview/api/...
    Django routes are defined as /api/..., so strip the app prefix.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get("PATH_INFO", "")
        match = CODER_APP_PREFIX_RE.match(path)
        if match:
            prefix = match.group(1)
            rest = match.group(2) or "/"
            request.META["SCRIPT_NAME"] = prefix
            request.META["PATH_INFO"] = rest
            # Django URL resolving uses request.path_info/path attributes.
            request.path_info = rest
            request.path = f"{prefix}{rest}" if rest.startswith("/") else f"{prefix}/{rest}"

        return self.get_response(request)
