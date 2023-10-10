"""App entry point tests."""
from unittest.mock import Mock, patch

from app.__main__ import main
from app.utils.common import Environment


@patch("app.__main__.parse_api_args", return_value=Environment.TEST)
@patch("uvicorn.run")
def test_main_api(uvicorn_run_mock: Mock, _: Mock) -> None:
    """Test main api function."""
    main()
    uvicorn_run_mock.assert_called()
