# coding: utf-8\n\r--------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="post_search_collection_request.py">
#   Copyright (c) 2018 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------


class PostSearchCollectionRequest(object):
    """
    Request model for post_search_collection operation.
    Initializes a new instance.
    :param name The Document name.
    :param search_options_collection_data Search Options Collection for corresponding Document Type.
    :param password Document password if required.
    :param folder The folder name.
    :param storage The file storage which have to be used.
    """

    def __init__(self, name, search_options_collection_data=None, password=None, folder=None, storage=None):
        self.name = name
        self.search_options_collection_data = search_options_collection_data
        self.password = password
        self.folder = folder
        self.storage = storage
